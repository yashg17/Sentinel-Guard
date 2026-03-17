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
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=ParentPortal \
                            -Dsonar.projectName='Parent Portal' \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://localhost:9000 \
                            -Dsonar.token=${env.SONAR_TOKEN}"
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
                sh 'docker compose up -d --force-recreate --remove-orphans'
            }
        }
    }

    post {
        always {
            sh 'docker image prune -f'
        }
    }
}
