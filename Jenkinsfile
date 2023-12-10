pipeline {
    agent any
    stages {
        stage('testing'){
            steps {
                sh(script: 'python3 detect.py --weights ./best.pt --source ./Pikachu.jpg')
            }
        }
    }
}