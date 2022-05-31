pipeline {
    agent {
       label "epyc-tempesta-test"
    }

    stages {
        stage('tempesta-test') {
            steps {
                echo 'FAKE MESSAGE'
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