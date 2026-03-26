pipeline {
    agent any
    environment {
        ECR_REPO = "<ECR_URL>/devops-app"
    }
    stages {
        stage('clone code'){
            steps {
                git 'https://github.com/satnamgrover/DevOps-python-app.git'
            }
        }
        stage('build and Tag Image'){
            steps{
                sh 'sudo docker build -t devops-app .'
                sh 'sudo docker tag devops-app:latest $ECR_REPO:latest'
            }
        }
        stage('push image to Registory'){
            steps{
                withCredentials([
                    string(credentialsId: 'aws_temp_access_key', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'aws_temp_secret_key', variable: 'AWS_SECRET_ACCESS_KEY'),
                    string(credentialsId: 'aws_temp_session_token', variable: 'AWS_SESSION_TOKEN')
                ])
                {
                sh '''
                set -e
                export DOCKER_CONFIG=$(pwd)/.docker
                mkdir -p $DOCKER_CONFIG
                aws sts get-caller-identity
                aws ecr get-login-password --region ap-south-1 | docker --config $DOCKER_CONFIG login --username AWS --password-stdin <ECR_URL>
                sudo docker --config $DOCKER_CONFIG push $ECR_REPO:latest
                '''
                }
            }
        
        }
        stage('Deploy code'){
            steps{
                sh 'kubectl apply -f k8s/Deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}
