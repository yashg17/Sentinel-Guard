pipeline {
    agent any
    environment {
        CLAUDE_API_KEY = credentials('CLAUDE_API_KEY')
        SONAR_TOKEN = credentials('SONAR_TOKEN')
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
            // We map the credential to an ENV variable to avoid the security warning
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
                timeout(time: 10, unit: 'MINUTES') { 
                    waitForQualityGate abortPipeline: true 
                }
            }
        }

        stage('Deploy HA') {
            steps {
                // Self-healing: clean up any failed network states before starting
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose up -d --force-recreate'
            }
        }
    } // End of stages

    post {
        always { 
            sh 'docker image prune -f' 
        }
    }
} // End of pipeline
