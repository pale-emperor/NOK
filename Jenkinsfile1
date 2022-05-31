pipeline {
    agent {
       label "epyc-tempesta-test"
    }

    stages {
        stage('Pull tempesta-test') {
            steps {
                echo 'FAKE'
                git url: 'https://github.com/tempesta-tech/tempesta-test.git'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}