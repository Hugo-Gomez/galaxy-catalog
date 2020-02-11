# Catalogue des galaxies

Le projet est déployé et en production à cette adresse :<br>
https://hugomez.pythonanywhere.com/

## Description du projet

API permettant d'acceder à des données scientifiques. Dans notre cas nous allons rendre accessible des données du catalogue Messier qui recense les objets extragalactiques.

## Technologies et version
- Python >= 3.7.1
- Flask >= 1.0.2
- SQLite >= 3.26.0

## Procedure d'installation
**Cloner ce dépôt :**<br>
<code>git clone https://github.com/Hugo-Gomez/galaxy-catalog.git</code>

**Installer les dépendances :**<br>
<code>pip3 install -r requirements.txt</code>

**Lancer l'application :**<br>
<code>python3 app.py</code>

## Documentation

**Get an object by Messier ID :**<br>
<code>/messier/object/M77</code>

**Get objects by filtering :**<br>
<code>/messier/objects?year=1780</code>

**Multi-Filtering is available :**<br>
<code>/messier/objects?year=1780&distance=8200</code>

**Available filters :**
- constellation
- discoverer
- year
- distance
- english_name
- french_name
- latin_name
- ra

## Auteurs

Hugo Gomez & Vincent Schuck
