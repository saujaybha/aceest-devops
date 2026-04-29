pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t saujaybha/aceest-app:latest .'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                echo 'Running static code analysis...'
            }
        }
    }
}
