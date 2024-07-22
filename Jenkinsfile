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
    }
}
