pipeline {
    agent any
    environment {
        ECR_REPO = "101992521948.dkr.ecr.ap-south-1.amazonaws.com/devops-app"
    }
    stages {
        stage('build code'){
            steps{
                sh 'sudo docker build -t devops-app .'
                sh 'sudo docker tag devops-app:latest $ECR_REPO:latest'
            }
        }
        stage('tag and push image'){
            steps{
                withCredentials([
                    string(credentialsId: 'aws_temp_access_key', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'aws_temp_secret_key', variable: 'AWS_SECRET_ACCESS_KEY'),
                    string(credentialsId: 'aws_temp_session_token', variable: 'AWS_SESSION_TOKEN')
                ])
                {
                sh '''
                aws sts get-caller-identity
                aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 101992521948.dkr.ecr.ap-south-1.amazonaws.com
                sudo docker push 101992521948.dkr.ecr.ap-south-1.amazonaws.com/devops-app:latest
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
