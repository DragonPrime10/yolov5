pipeline {
    agent any
    stages {
        stage('testing'){
            steps {
                sh(script: 'python detect.py --weights ./best.pt --source ./Pikachu.jpg')
            }
        }
    }
}