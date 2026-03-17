pipeline {
    agent any
    environment {
        CLAUDE_API_KEY = credentials('CLAUDE_API_KEY')
        SONAR_TOKEN = credentials('SONAR_TOKEN')
    }
    stages {
        stage('Build') {
            steps { sh 'docker compose build' }
        }
        stage('SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube'
                    // This masks the secret and prevents the "Groovy interpolation" warning
                    withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_AUTH_TOKEN')]) {
                        withSonarQubeEnv('SonarQube') {
                            // Using single quotes (') ensures the shell handles the variable, not Groovy.
                            sh "'${scannerHome}/bin/sonar-scanner' " +
                               "-Dsonar.projectKey=ParentPortal " +
                               "-Dsonar.projectName='Parent Portal' " +
                               "-Dsonar.sources=. " +
                               "-Dsonar.host.url=http://34.229.95.117:9000 " +
                               "-Dsonar.token=${SONAR_AUTH_TOKEN}"
                        }
                    }
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 10, unit: 'MINUTES') { waitForQualityGate abortPipeline: true }
            }
        }
        stage('Deploy HA') {
            steps {
                // Self-healing: clean up any failed network states before starting
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose up -d --force-recreate'
            }
        }
    }
    post {
        always { sh 'docker image prune -f' }
    }
}
