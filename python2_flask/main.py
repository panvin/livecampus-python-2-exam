from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import find_dotenv, load_dotenv
from datetime import datetime
import mysql.connector
import jwt
import os

# Récupération des secret présent dans le fichier .env
load_dotenv(find_dotenv())

# Initialisation de mon app Flask
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
# paramétrage CORS pour autoriser les requêtes venant de l'appli Dkango
CORS_HEADERS = 'Content-Type, Authorization, Origin, x-csrf-token, Access-Control-Allow-Credentials' 
CORS_METHODS = 'POST, OPTIONS' 
CORS_ORIGINS = ['http://127.0.0.1:8000', 'http://localhsot:8000']

CORS(app, headers=CORS_HEADERS, methods=CORS_METHODS, origins=CORS_ORIGINS, supports_credentials=True)

# Création de la connection à la base de donnée"
db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE')
)

jwt_secret_key = os.getenv('JWT_SECRET_KEY')

# Méthode ajouté pour supprimer une e
@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()
    
@app.route('/<string:url>', methods=["POST"])
@cross_origin(origins ="*")
def updateSurvey(url):
    try:
        #Je récupère le token
        token     = request.cookies.get('jwt')
        payload   = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        userId    = payload['userId']
        username  = payload['username']
        sessionId = payload['sessionId']

        if request.is_json:
            data = request.json
            dateSend = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

            currentUserAnswer = getRecordForCurrentUser(userId, sessionId)
            if currentUserAnswer:
                response = updateRecordForUser(userId, sessionId, data, dateSend)
            else:
                response = createRecordForUser(userId, sessionId, data, dateSend)
        else:
            response = jsonify({ 'error' : 'Les données envoyées ne sont pas au format json'}) 

        return  response
    except jwt.ExpiredSignatureError as error:
        response = jsonify({ 'data' :f'Erreur {error}'})
        return response
    except jwt.InvalidTokenError:
        response = jsonify({ 'data' :f'Erreur {error}'})
        
        #response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    
def getRecordForCurrentUser (user: str, sessionId: str):

    sql = "SELECT id FROM  python2_django_surveyanswer WHERE session_id = %s and student_id = %s"
    parametersAsTuple = (user, sessionId)

    cursor = db.cursor(prepared=True)
    cursor.execute(sql, parametersAsTuple)
    answer = cursor.fetchone()
    cursor.close()

    return answer

def createRecordForUser(userId: str, sessionId: str, data: dict, dateSend: str) -> Response:

    percentageValue  = data.get("percentage")
    progressionValue = data.get("progression")
    difficultyValue  = data.get("difficulty")

    sql = "INSERT INTO python2_django_surveyanswer (percentage, progression, difficulty, dateSend, dateInitialSend, session_id, student_id ) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    val = (percentageValue, progressionValue, difficultyValue, dateSend, dateSend, sessionId, userId )
    cursor = db.cursor(prepared=True)
    try:
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        response = jsonify("data", "Nouvelle ligne ajoutée à l'enquête")
    except Exception as error:
        cursor.close()
        response = jsonify ("error", f"Insert - {error}")
        print(progressionValue)
        print(error)

    return response

def updateRecordForUser(userId: str, sessionId: str, data: dict, dateSend: str) -> Response:
    print("Mise à jour")
    queryFragmentAsList=[]
    valuesList=[]

    queryFragmentAsList.append("dateSend = %s")
    valuesList.append(dateSend)

    if "progression" in data:
        queryFragmentAsList.append("progression = %s")
        progressionValue = data.get("progression")
        valuesList.append(progressionValue)

    if "difficulty" in data:
        queryFragmentAsList.append("difficulty = %s")
        difficultyValue = data.get("difficulty")
        valuesList.append(difficultyValue)

    if "percentage" in data:
        queryFragmentAsList.append("percentage = %s")
        percentageValue = data.get("percentage")
        valuesList.append(percentageValue)


    queryFragmentAsString = ", ".join(queryFragmentAsList)
    sql = f"UPDATE python2_django_surveyanswer set {queryFragmentAsString} where session_id = %s and student_id = %s;"
    val = tuple(valuesList + [sessionId, userId ])

    cursor = db.cursor(prepared=True)
    try:
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        response = jsonify({"data" : "Ligne mise à jour"})
    except Exception as error:
        cursor.close()
        response = jsonify({"error" : f"Erreur à l'insertion de la ligne {error}"})
        print(error)

    return response

if __name__ == "__main__":
    app.run(debug=True)