pipeline {
    agent any
    environment {
        // Only keep what you actually use in the shell steps
        CLAUDE_API_KEY = credentials('CLAUDE_API_KEY')
    }
    stages {
        stage('Build') {
            steps { 
                sh 'docker compose build' 
            }
        }
        
        stage('SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube'
                    // Securely pass the token via env variable
                    withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN_ENV')]) {
                        withSonarQubeEnv('SonarQube') {
                           sh """
                            ${scannerHome}/bin/sonar-scanner \
                                -Dsonar.projectKey=ParentPortal \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=http://172.31.25.22:9000 \
                                -Dsonar.token=\$SONAR_TOKEN_ENV \
                                -Dsonar.exclusions='**/venv/**,**/node_modules/**,**/.docker/**,**/__pycache__/**'
                            """
                        }
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // This waits for the webhook from SonarQube
                timeout(time: 5, unit: 'MINUTES') { 
                    waitForQualityGate abortPipeline: true 
                }
            }
        }

        stage('Deploy HA') {
            steps {
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose up -d --force-recreate'
            }
        }
    } 

    post {
        always { 
            sh 'docker image prune -f' 
        }
    }
}
