pipeline {
    agent {
       label "epyc-tempesta-test"
    }

    stages {
        stage('Pull-tempesta-test') {
            steps {
                echo 'FAKE'
                git 'https://github.com/tempesta-tech/tempesta-test.git'
            }
        }
    }
}