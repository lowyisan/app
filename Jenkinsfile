pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git url: 'http://git-server:3000/repository.git', branch: 'main'
            }
        }
        stage('OWASP DependencyCheck') {
            steps {
                script {
                    dependencyCheck additionalArguments: '--format HTML --format XML --noupdate', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
                    dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
            }
        }
        stage('Code Quality Check via SonarQube') {
            environment {
                SONARQUBE_TOKEN = credentials('sq')
            }
            steps {
                script {
                    def scannerHome = tool 'SonarQube';
                    // Print the path of SonarQube scanner
                    sh "echo SonarQube Scanner Path: ${scannerHome}"

                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=app -Dsonar.sources=. -Dsonar.host.url=http://192.168.0.210:9000 -Dsonar.token=${SONARQUBE_TOKEN}"
                    }
                }
            }
        }
    }
}
