# house-price-api
Déploiement d'une API de prédiction du prix des maisons avec CI/CD

from datetime import date

today = date.today().strftime("%d/%m/%Y")

readme_content = f"""# 🏠 house-price-api
**Déploiement d'une API de prédiction du prix des maisons avec CI/CD**

---

## 🧠 Contexte

Ce projet a été réalisé dans le cadre de mon apprentissage des pratiques DevOps et MLOps. Il vise à développer une API de prédiction de prix de maisons, conteneurisée avec Docker, déployable automatiquement grâce à un pipeline CI/CD sous GitLab CI et Jenkins.

---

## 🎯 Objectifs

- Développer une API REST avec FastAPI pour prédire le prix des maisons.
- Conteneuriser l’application avec Docker.
- Mettre en place un pipeline CI/CD avec GitLab pour automatiser build, test, push et déploiement.
- Intégrer Jenkins comme alternative de CI.
- Exécuter et tester l'API localement avec Docker.

---

## 🧱 Architecture Technique

FastAPI → Docker → GitLab CI/CD → GitLab Registry → Jenkins

---

## 📦 Technologies Utilisées

- FastAPI
- Python 3.10+
- Docker
- GitLab CI/CD
- Jenkins (optionnel)
- Scikit-learn
- Uvicorn

---

## ⚙️ CI/CD

### GitLab CI/CD
- Pipeline défini dans `.gitlab-ci.yml`
- Étapes : `build`, `push`, `deploy`
- Image Docker automatiquement poussée vers `registry.gitlab.com`

### Jenkins (optionnel)
- Pipeline défini dans `Jenkinsfile`
- Authentification sécurisée via token
- Étapes similaires au pipeline GitLab

---

## 🚀 Lancer le projet en local

```bash
git clone https://gitlab.com/khoty-wolie/house-price-api.git
cd house-price-api
docker build -t house-price-api .
docker run -d -p 8000:8000 house-price-api

---

Exemple d’appel à l’API

POST http://localhost:8000/predict
Content-Type: application/json

{
  "features": [3, 2, 120, 1, 0]
}


📁 Arborescence


house-price-api/
│
├── app/                     # Code source de l’API
│   └── main.py              # Entrée principale de FastAPI
│
├── tests/                   # Tests unitaires (si existants)
│
├── Dockerfile               # Configuration Docker
├── requirements.txt         # Dépendances Python
├── .gitlab-ci.yml           # Pipeline CI/CD GitLab
├── Jenkinsfile              # Pipeline Jenkins
└── README.md                # Documentation du projet


Résultat

Pipeline GitLab fonctionnel et testé avec succès ✅

Dockerisation de l’API vérifiée ✅

API disponible sur http://localhost:8000 après build ✅

Jenkins prêt à relayer ou compléter la CI ✅


📚 Ressources Utiles
FastAPI Docs

GitLab CI/CD Pipelines

Jenkins Pipeline

Docker Introduction

Sklearn Docs
