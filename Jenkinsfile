pipeline {
    agent any

    environment {
        IMAGE_NAME = "khoty-wolie/house-price-api"
        DOCKER_REGISTRY = "registry.gitlab.com"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://gitlab.com/khoty-wolie/house-price-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_REGISTRY/$IMAGE_NAME:latest ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'gitlab-docker-credentials', url: "https://$DOCKER_REGISTRY"]) {
                    sh "docker push $DOCKER_REGISTRY/$IMAGE_NAME:latest"
                }
            }
        }

        stage('Deploy') {
            steps {
                sh "docker run -d -p 8000:8000 $DOCKER_REGISTRY/$IMAGE_NAME:latest"
            }
        }
    }
}
