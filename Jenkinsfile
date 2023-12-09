pipeline {
    agent any
    stages {
        stage('setup'){
            steps {
                sh(script: 'pip install requirements.txt)
            }
        }
        stage('testing'){
            steps {
                sh(script: 'python detect.py --weights ./runs/train/exp9/weights/best.pt --source ./Pikachu.jpg')
            }
        }
    }
}