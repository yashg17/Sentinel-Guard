pipeline {
    agent any
    
    environment {
        // Ensure these IDs exist in Jenkins Credentials
        CLAUDE_API_KEY = credentials('CLAUDE_API_KEY')
        SONAR_TOKEN = credentials('SONAR_TOKEN')
    }

    stages {
        stage('Build') {
            steps {
                // Building images using the docker-compose.yml in your repo
                sh 'docker compose build'
            }
        }

        stage('SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube'
                    withSonarQubeEnv('SonarQube') {
                        // Added -Dsonar.working.directory to ensure the report file is generated correctly
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=ParentPortal \
                            -Dsonar.projectName='Parent Portal' \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://localhost:9000 \
                            -Dsonar.working.directory=.scannerwork"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    // This waits for the webhook back from SonarQube
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Deploy HA') {
            steps {
                // Deploys the containers in detached mode
                sh 'docker compose up -d --force-recreate --remove-orphans'
            }
        }
    }

    post {
        always {
            // Cleans up dangling images to save EC2 space
            sh 'docker image prune -f'
        }
    }
}
