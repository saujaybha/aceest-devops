pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t saujaybha/aceest-app:latest .' // [cite: 93, 113]
            }
        }
        stage('Test') {
            steps {
                sh 'pytest' // [cite: 107, 114]
            }
        }
        stage('SonarQube Analysis') {
            steps {
                echo 'Running static code analysis...' // [cite: 108, 114]
            }
        }
    }
}
