# 🏠 house-price-api  
**Déploiement d'une API de prédiction du prix des maisons avec CI/CD**

---

## 📘 Contexte

Ce projet a été réalisé dans le cadre de mon apprentissage des pratiques **DevOps** et **MLOps**. L'objectif est de développer une API REST permettant de prédire le prix de maisons à partir de données simples. Cette API est conteneurisée avec Docker et intégrée dans une chaîne d’automatisation CI/CD à l’aide de **GitLab CI/CD** et **Jenkins**.

---

## 🎯 Objectifs

- Développer une API REST avec **FastAPI**.
- Conteneuriser l’application avec **Docker**.
- Mettre en place un pipeline **CI/CD** sous **GitLab** pour :
  - Construire l’image Docker.
  - Exécuter des tests (si présents).
  - Pousser l’image vers le **GitLab Container Registry**.
  - Déployer automatiquement l’API.
- Intégrer une alternative CI avec **Jenkins**.
- Permettre l'exécution locale de l’API avec Docker.

---

## 🧱 Architecture Technique

```
FastAPI → Docker → GitLab CI/CD → GitLab Container Registry → Jenkins
```

---

## ⚙️ Technologies Utilisées

- Python 3.10+
- FastAPI
- Scikit-learn
- Docker
- GitLab CI/CD
- Jenkins (optionnel)
- Uvicorn

---

## 🔁 CI/CD

### 🧪 GitLab CI/CD

- Pipeline défini dans le fichier `.gitlab-ci.yml`
- Étapes du pipeline :
  - `build` : construction de l’image Docker
  - `push` : push vers `registry.gitlab.com`
  - `deploy` : exécution de l’image localement ou sur serveur distant

### 🔧 Jenkins (optionnel)

- Pipeline défini dans le fichier `Jenkinsfile`
- Authentification sécurisée avec token GitLab
- Étapes similaires à GitLab CI : `checkout`, `build`, `push`, `deploy`

---

## 🚀 Lancer le projet en local

```bash
git clone https://gitlab.com/khoty-wolie/house-price-api.git
cd house-price-api
docker build -t house-price-api .
docker run -d -p 8000:8000 house-price-api
```

---

### 📡 Exemple d'appel à l’API

```http
POST http://localhost:8000/predict
Content-Type: application/json

{
  "features": [3, 2, 120, 1, 0]
}
```

---

## 📁 Arborescence du Projet

```
house-price-api/
│
├── app/                     # Code source de l’API
│   └── main.py              # Point d’entrée de FastAPI
│
├── tests/                   # Tests unitaires (si présents)
│
├── Dockerfile               # Instructions pour l’image Docker
├── requirements.txt         # Dépendances Python
├── .gitlab-ci.yml           # Pipeline CI/CD GitLab
├── Jenkinsfile              # Pipeline Jenkins (optionnel)
└── README.md                # Documentation du projet
```

---

## ✅ Résultats

- ✅ Pipeline GitLab CI/CD fonctionnel
- ✅ Image Docker générée et testée avec succès
- ✅ API accessible via `http://localhost:8000`
- ✅ Jenkins prêt à compléter ou remplacer GitLab CI

---

## 📚 Ressources Utiles

- [📘 FastAPI Documentation](https://fastapi.tiangolo.com/)
- [🔧 GitLab CI/CD Guide](https://docs.gitlab.com/ee/ci/)
- [⚙️ Jenkins Pipelines](https://www.jenkins.io/doc/book/pipeline/)
- [🐳 Docker Introduction](https://docs.docker.com/get-started/)
- [📊 Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
