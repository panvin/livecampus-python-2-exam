from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import find_dotenv, load_dotenv
import mysql.connector
import jwt
import os

# Récupération des secret présent dans le fichier .env
load_dotenv(find_dotenv())

# Initialisation de mon app Flask
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
# paramétrage CORS pour autoriser les requêtes venant de l'appli Dkango
CORS(app, headers='Content-Type', methods="POST", supports_credentials=True)

# Création de la connection à la base de donnée"
db = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE')
)

jwt_secret_key = os.getenv('JWT_SECRET_KEY')

@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()
    
@app.route('/<string:url>', methods=["POST"])
@cross_origin(origins ="*")
def updateSurvey(url):
    try:
        #Je récupère le token
        token = request.cookies.get('jwt')
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        userId = payload['userId']
        username = payload['username']
        sessionId = payload['sessionId']
        print(f"ok - {username} - {sessionId} - {token}")

        if request.is_json:
            data = request.json
            if isRecordPresentForUser(userId, sessionId):
                updateRecordForUser(userId, sessionId, data)
            else:
                createRecordForUser(userId, sessionId, data)

        else:
            response = jsonify({ 'Error' : 'Les données envoyées ne sont pas au format json'}) 
            return  response

        response = jsonify({ 'data' : f'Bienvenue à toi {username}, ton accès à la session {sessionId} a été pris en compte'})
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return  response
    except jwt.ExpiredSignatureError:
        response = jsonify({ 'data' :f'Erreur'})
        return response
    except jwt.InvalidTokenError:
        response = jsonify({ 'data' :f'Erreur'})
        return response
    
def isRecordPresentForUser (user, sessionId):

    sql = "SELECT id FROM  python2_django_surveyanswer WHERE session_id = %s and student_id = %s"
    parametersAsTuple = (user, sessionId)

    cursor = db.cursor(prepared=True)
    cursor.execute(sql, parametersAsTuple)
    answer = cursor.fetchall()
    cursor.close()

    return bool(answer)

def createRecordForUser(userId, sessionId, data):
    print("Creation")

def updateRecordForUser(userId, sessionId, data):
    print("Mise à jour")

if __name__ == "__main__":
    app.run(debug=True)