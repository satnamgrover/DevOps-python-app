pipeline {
    agent any
    
    stages {
        stage('prepare variables')
        {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'Docker_User', passwordVariable: 'Docker_Pass')])
                {
                    script {
                        env.DOCKER_IMAGE = "${Docker_User}/python-app"
                    }
                }
            }
        }
        stage('build docker image'){
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }
        stage('push image to docker hub'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'Docker_user', passwordVariable: 'Docker_Pass')])
                {
                    sh '''
                    echo $Docker_Pass | docker login -u $Docker_user --password-stdlin
                    docker push $DOCKER_IMAGE
                    '''
                }
            }
        }
        stage('deploy using kubernetes'){
            steps{
                sh "kubectl apply -f k8s/Deployment.yaml"
                sh "kubectl apply -f k8s/service.yaml"
            }
        }
        
    }
}
