pipeline {
    agent any
    stages {
        stage('setup'){
            steps {
                sh(script: 'pip install requirements.txt')
            }
        }
        stage('testing'){
            steps {
                sh(script: 'python detect.py --weights ./best.pt --source ./Pikachu.jpg')
            }
        }
    }
}