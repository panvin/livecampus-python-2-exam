# Projet examen Python 2
## **Parcours ECI P2025 - Livecampus** - **Auteur:** Vincent PANOUILLERES

### Pré-requis:
- Mariadb server
- Python 3  
(Le développement a été réalisés sou machine Linux, via Visual Studio Code)

### Mise en route du projet:

Les secret sont à mettre dans un fichier .env à la racine du projet (les valeurs sont à adapter).  
Un fichier .env.default est présent dans le projet pour donner la structure des données.  

1. Créer une base de donnée 'maDatabaseProjet' :
```sql
CREATE DATABASE maDatabaseProjet; 
```
2. Créer un utilisateur pour accéder à la base
```sql
GRANT ALL ON maDatabaseProjet.* TO monUserDeDB@localhost IDENTIFIED BY 'monPasswordTotalementInsecure';
FLUSH PRIVILEGES;
```
3. Importer le dump projet.sql dans la base 'maDatabaseProjet'
```
mysql maDatabaseProjet < maDatabaseProjet.sql
```
4. Créer un environnement virtuel dans le répertoire du projet
5. Installer les dépendances projet:
 ```
pip install -r requirements.txt
```
6. **Créer et remplir le fichier .env** à la racine (copier le contenu de .env.default et adapter si besoin)
7. Ouvrir un premier terminal (avec venv) et lancer l'application Django:
```
python manage.py runserver
```
8. Ouvrir un second terminal (avec venv) et lancer l'appli Flask:
```
python python2_flask/main.py
```

### Accéder à l'application:
L'application est disponible à l'adresse: http://127.0.0.1:8000/  
L'url de l'API Flask est: http://127.0.0.1:5000  

Les permissions des pages ont été définies via les groupes Django.  
Les étudiants peuvent visualiser la page d'acceuil et le formulaire d'enquête.  
Les enseignants peuvent tout voir mais ils ne sont pas pris en compte par l'API Flask s'ils se connectent à une enquête  

| login   |  password  | groupe  | admin | 
|---------|------------|---------|-------|
| vincent | =Test12345 | teacher | yes   | 
| aline   | =Test12345 | teacher | yes   | 
| lucy    | =Test12345 | student | no    |
|  marc   | =Test12345 | student | no    |


### Sources:

Voici les liens vers les différentes ressources utilisées pour mener à bien le projet:  

<https://www.w3schools.com/>  
<https://docs.djangoproject.com/en/5.0/>  
<https://stackoverflow.com/>  
<https://getbootstrap.com/docs/5.0/getting-started/introduction/>

