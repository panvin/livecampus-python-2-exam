from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import find_dotenv, load_dotenv
from datetime import datetime
from dbhelper import DatabaseHelper
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

CORS(app, headers=CORS_HEADERS, methods=CORS_METHODS, origins=CORS_ORIGINS, supports_credentials=True, max_age=3600)

jwt_secret_key = os.getenv('JWT_SECRET_KEY')

# Création de l'objet Database
db = DatabaseHelper()

# Pré-flight request pour CORS
@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()

# Méthode de mise à jour des élément de notre API
@app.route('/<string:url>', methods=["POST"])
@cross_origin(origins ="*")
def updateSurvey(url):
    try:
        # Récupération du token JWT
        token     = request.cookies.get('jwt')
        payload   = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        userId    = payload['userId']
        username  = payload['username']
        sessionId = payload['sessionId']

        # Ensemble de tests avant de mettre à jour les données en DB
        if request.is_json:
            data = request.json
            dateSend = datetime.utcnow()
            
            if checkStudentGroup(userId):
                
                if checkInputValidity(data):

                    if checkSessionValidity(sessionId, dateSend):

                        currentUserAnswer = db.getRecordForCurrentUser(userId, sessionId)
                        dateSendAsString = dateSend.strftime('%Y-%m-%d %H:%M:%S.%f')

                        if currentUserAnswer:
                            response = db.updateRecordForUser(userId, sessionId, data, dateSendAsString)
                        else:
                            response = db.createRecordForUser(userId, sessionId, data, dateSendAsString)

                    else:
                        response = jsonify({ 'error' : 'La session demandée n\'est pas ouverte'})    
                else: 
                    response = jsonify({ 'error' : 'Les données envoyées n\'ont pas un format valide'})
            else:
                response = jsonify({ 'error' : 'L\'utilisateur ne fais pas partie du groupe étudiant'})
        else:
            response = jsonify({ 'error' : 'Les données envoyées ne sont pas au format json'}) 

        return  response
    except jwt.ExpiredSignatureError as error:
        response = jsonify({ 'error' : 'Le jeton JWT est expiré'})
        return response
    except jwt.InvalidTokenError:
        response = jsonify({ 'error' : 'Le jeton JWT est invalide'})
        
        #response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response
    
# Vérification des données envoyées par la page de formulaire
def checkInputValidity(data):
    
    listDifficulties = ['EA','NO','HA','VA','EX']
    listProgressions = ['AC','IP','NA']
    areListValid =  data.get("progression") in listProgressions and data.get("difficulty") in listDifficulties 

    try:
        isPercentageValid = 0 <= int(data.get("percentage")) <= 100 
    except Exception:
        isPercentageValid = False

    return areListValid and isPercentageValid

# Vérification de l'appartenance de l'utilisateur au groupe étudiant
def checkStudentGroup(userId: str):
    return db.getUserFromGroupStudent(userId)

# Vérification de la validité de la session qui doit être mise à jour
def checkSessionValidity(sessionId: str, dateSend: datetime):
    currentSession = db.getCurrentSession(sessionId)

    isSessionValid    = currentSession[0]
    isSessionInFuture = dateSend < currentSession[1]
    isSessionOver     = dateSend > currentSession[2]

    return isSessionValid and not isSessionOver and not isSessionInFuture


if __name__ == "__main__":
    app.run(debug=True)