pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git url: 'https://github.com/lowyisan/app.git', branch: 'main'
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
            steps {
                script {
                    def scannerHome = tool 'SonarQube';
                    // Print the path of SonarQube scanner
                    sh "echo SonarQube Scanner Path: ${scannerHome}"

                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=app -Dsonar.sources=. -Dsonar.host.url=http://<your ip address>:9000 -Dsonar.token=sqp_3fb79bead259471852eab972a856a26e7f3a4ac8"
                    }
                }
            }
        }
    }
}
