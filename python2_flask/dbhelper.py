from flask import Response, jsonify
import mysql.connector
import os

class DatabaseHelper:
    # Création de la connection à la base de donnée"
    def __init__(self):
        self.db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE')
        )
    
    # Méthode de récupération de la réponse pour une session donnée et  un étudiant donné
    def getRecordForCurrentUser (self,userId: str, sessionId: str):

        sql = "SELECT * FROM  python2_django_surveyanswer WHERE session_id = %s and student_id = %s"
        parametersAsTuple = (sessionId,userId)

        cursor = self.db.cursor(prepared=True)
        cursor.execute(sql, parametersAsTuple)
        answer = cursor.fetchone()
        cursor.close()
        return answer
    
    # Méthode de récupération de la session à partir de son Id
    def getCurrentSession (self,sessionId: str):

        sql = "SELECT status, dateStarted, dateEnd FROM  python2_django_sessionsurvey WHERE id = %s"
        parametersAsTuple = (sessionId,)

        cursor = self.db.cursor(prepared=True)
        cursor.execute(sql, parametersAsTuple)
        answer = cursor.fetchone()
        cursor.close()

        return answer
    
    def getUserFromGroupStudent(self, userId: str):

        sql = "SELECT auth_group.name FROM auth_user_groups INNER JOIN auth_group ON auth_user_groups.group_id = auth_group.id WHERE user_id = %s AND auth_group.name='student';"
        parametersAsTuple = (userId,)

        cursor = self.db.cursor(prepared=True)
        cursor.execute(sql, parametersAsTuple)
        answer = cursor.fetchone()
        cursor.close()

        return answer

    # Méthode permettant l'insertion des réponses d'enquête en base de donnée pour un utilisateur
    def createRecordForUser(self, userId: str, sessionId: str, data: dict, dateSend: str) -> Response:

        percentageValue  = data.get("percentage")
        progressionValue = data.get("progression")
        difficultyValue  = data.get("difficulty")

        sql = "INSERT INTO python2_django_surveyanswer (percentage, progression, difficulty, dateSend, dateInitialSend, session_id, student_id ) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        val = (percentageValue, progressionValue, difficultyValue, dateSend, dateSend, sessionId, userId )
        cursor = self.db.cursor(prepared=True)
        try:
            cursor.execute(sql, val)
            self.db.commit()
            cursor.close()
            response = jsonify("data", "Nouvelle ligne ajoutée à l'enquête")
        except Exception as error:
            cursor.close()
            response = jsonify ("error", "Une erreur de base de donée est survenue")
            print(error)

        return response

    # Méthode permettant de mettre à jour les données d'enquête pour un utilisateur
    def updateRecordForUser(self, userId: str, sessionId: str, data: dict, dateSend: str) -> Response:

        # Création de la requête SQL et du Tuple de valeurs à ajouter 
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

        cursor = self.db.cursor(prepared=True)
        try:
            cursor.execute(sql, val)
            self.db.commit()
            cursor.close()
            response = jsonify({"data" : "Ligne mise à jour"})
        except Exception as error:
            cursor.close()
            response = jsonify({"error" : "Une erreur de base de donée est survenue"})
            print(error)

        return response