from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector
import jwt

mydb = mysql.connector.connect(
    host="localhost",
    user="userDB",
    password=env.conf["dbPassword"],
    database="PROJET"
)

#initialise mon app Flask
app = Flask(__name__)
CORS(app, headers='Content-Type', methods="POST", supports_credentials=True)
#app.secret_key = env.conf["secretLocal"]
jwt_secret_key = "test_12345"

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
        print(request.cookies.getlist('jwt'))
        print(url)
        print(token)
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        username = payload['username']
        sessionId = payload['sessionId']
        print(f"ok - {username} - {sessionId} - {token}")
        response = jsonify({ 'data' : f'Bienvenue à toi {username}, ton accès à la session {sessionId} a été pris en compte'})
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return  response
    except jwt.ExpiredSignatureError:
        response = jsonify({ 'data' :f'Erreur'})
        return response
    except jwt.InvalidTokenError:
        response = jsonify({ 'data' :f'Erreur'})
        return response

if __name__ == "__main__":
    app.run(debug=True)