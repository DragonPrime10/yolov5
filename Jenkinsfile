pipeline {
    agent any
    stages {
        stage('setup'){
            steps {
                sh(script: 'pip install -r requirements.txt')
            }
        }
        stage('testing'){
            steps {
                sh(script: 'python3 detect.py --weights ./best.pt --source ./Pikachu.jpg')
                sh(script: 'python3 detect.py --weights ./best.pt --source ./DronePhotography1.jpg')
                sh(script: 'python3 detect.py --weights ./best.pt --source ./Cat.jpeg')
                sh(script: 'python3 detect.py --weights ./best.pt --source ./Dog.jpeg')
                sh(script: 'python3 detect.py --weights ./best.pt --source ./Person.jpeg')

            }
        }
    }
}