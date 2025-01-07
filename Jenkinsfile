pipeline {
    agent any

    environment {
        // Define paths and tokens for tools
        ZAP_URL = 'http://localhost:8080' // OWASP ZAP local URL
        SONARQUBE_SERVER = 'http://localhost:9000' // SonarQube server URL
        SONARQUBE_TOKEN = credentials('sonarqube-auth-token') // Add SonarQube token to Jenkins credentials
        DEPLOYMENT_ENV = 'staging' // Example deployment environment
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub repository...'
                git branch: 'main', url: 'https://github.com/Rudra2018/Bug-Bounty-Scripts'
            }
        }

        stage('Static Analysis (SonarQube)') {
            steps {
                echo 'Running SonarQube SAST...'
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=BugBountyScripts \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=$SONARQUBE_SERVER \
                    -Dsonar.login=$SONARQUBE_TOKEN
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'echo "No build process defined for scripts. Skipping build..."'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "No specific tests defined for scripts. Skipping tests..."'
            }
        }

        stage('Dynamic Analysis (OWASP ZAP)') {
            steps {
                echo 'Running OWASP ZAP DAST...'
                sh '''
                zap-baseline.py -t http://localhost:8080 -r zap-report.html || echo "DAST failed, check logs!"
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'zap-report.html', allowEmptyArchive: true
                }
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to $DEPLOYMENT_ENV environment..."
                sh '''
                echo "This is a placeholder for deployment steps. Update as needed."
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
