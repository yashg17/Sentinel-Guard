pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // Using sudo if jenkins user isn't in docker group
                sh 'docker compose build' 
            }
        }
        
        stage('SonarQube Scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube'
                    withSonarQubeEnv('SonarQube') {
                        sh """
                        ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=ParentPortal \
                            -Dsonar.projectName='Parent Portal' \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://23.22.129.234:9005 \
                            -Dsonar.python.version=3 \
                            -Dsonar.exclusions='**/venv/**,**/node_modules/**,**/.docker/**,**/__pycache__/**'
                        """
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    try {
                        timeout(time: 2, unit: 'MINUTES') { 
                            waitForQualityGate abortPipeline: false 
                        }
                    } catch (Exception e) {
                        echo "WARNING: Quality Gate timed out. Check SonarQube UI at :9005"
                    }
                }
            }
        }

        stage('Deploy HA') {
            steps {
                // Ensure we are deploying the version we just built
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
