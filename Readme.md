# Projet examen Python 2
## **Parcours ECI P2025 - Livecampus**
## **Auteur:** Vincent PANOUILLERES

## Pré-requis:
- Mariadb server
- Python 3
(Le développement a été réalisés sou machine Linux, via Visual Studio Code)

## Mise en route du projet:

Les secret sont à mettre dans un fichier .env à la racine du projet (les valeurs sont à adapter). 
Un fichier .env.default est présent dans le projet pour donner la structure des données

1. Créer une base de donnée "PROJET" :
```sql
CREATE DATABASE 'maDatabaseProjet'; 
```
2. Créer un utilisateur pour accéder à la base
```sql
GRANT ALL ON 'maDatabaseProjet'.'*' TO 'monUserDeDB'@'localhost' IDENTIFIED BY 'monPasswordTotalementInsecure'; 
FLUSH PRIVILEGES;
```
3. Importer le dump projet.sql dans la base 'maDatabaseProjet'
4. Créer un environnement virtuel dans le répertoire du projet
5. Installer les dépendances projet:
 ```
pip -r requirements.txt
```
5. Ouvrir un premier terminal (avec venv) et lancer l'application Django:
```
python manage.py runserver
```
6. Ouvrir un second terminal (avec venv) et lancer l'appli Flask:
```
python python2_flask/main.py
```

## Accéder à l'application:
L'application est disponible à l'adresse: http://127.0.0.1:8000/