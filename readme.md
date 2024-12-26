# Projet Django

Ce projet est une application Django configurée pour l'authentification utilisateur via email, la gestion des utilisateurs personnalisés, et une interface utilisateur simple pour se connecter et consulter son profil.

## Prérequis

- Python 3.9 ou version ultérieure
- pip (installé avec Python)
- Un environnement virtuel (optionnel mais recommandé)

## Installation

1. Clonez ce dépôt :
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DEPOT>

2. Installez les dépendances :
   pip install -r requirements.txt

3. Configurez les variables d'environnement dans un fichier `.env` à la racine du projet. Par exemple :
   DJANGO_SECRET_KEY='votre-clé-secrète-django'

4. Appliquez les migrations :
   python manage.py migrate

5. Lancez le serveur de développement :
   python manage.py runserver

Accédez à l'application dans votre navigateur à l'adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Fonctionnalités

### Authentification personnalisée

- Utilisation d'un modèle d'utilisateur personnalisé (CustomUser) avec email comme identifiant principal.
- Gestion des utilisateurs via Django Admin.
- Prise en charge de la vérification par email grâce à Django Allauth.

### Interface utilisateur

- Une page de connexion (`login.html`).
- Une page de profil (`profile.html`) affichant les informations de l'utilisateur connecté.

## Test et qualité

- Tests unitaires pour le modèle `CustomUser` avec `pytest`.
- Configuration de `pytest` disponible dans `pytest.ini`.

## Structure du projet

- `models.py` : Modèle utilisateur personnalisé.
- `views.py` : Vue pour la redirection et la page de profil.
- `urls.py` : Routage des URLs de l'application.
- `templates/` : Templates HTML avec gestion de l'authentification.
- `static/css/style.css` : Fichier CSS pour le style de l'application.
- `requirements.txt` : Liste des dépendances Python.
- `.env` : Variables d'environnement (exemple inclus).

## Tests

Pour exécuter les tests :
pytest

## Déploiement

### Fichiers statiques

Pour préparer les fichiers statiques pour la production :
python manage.py collectstatic

### Production avec WSGI

Utilisez le fichier `wsgi.py` pour configurer le projet avec un serveur WSGI tel que Gunicorn ou uWSGI.

### ASGI pour WebSockets

Le fichier `asgi.py` est inclus pour les configurations nécessitant le protocole ASGI (ex : WebSockets).

## Contributeurs

KillianP