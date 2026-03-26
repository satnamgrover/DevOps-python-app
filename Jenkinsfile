pipeline {
    agent any
    environment {
        ECR_REPO = "101992521948.dkr.ecr.ap-south-1.amazonaws.com/devops-app"
    }
    stages {
        stage('build code'){
            steps{
                sh 'sudo docker build -t devops-app .'
            }
        }
        stage('tag and push image'){
            steps{
                sh 'sudo docker tag devops-app:latest $ECR_REPO:latest'
                sh '''
                aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 101992521948.dkr.ecr.ap-south-1.amazonaws.com
                docker push 101992521948.dkr.ecr.ap-south-1.amazonaws.com/devops-app:latest
                '''
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
