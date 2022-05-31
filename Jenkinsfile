pipeline {
    agent {
       label "epyc-tempesta-test"
    }

    stages {
        stage('tempesta') {
            steps {
                echo 'FAKE1'
                git url: 'https://github.com/tempesta-tech/tempesta-test.git'
            }
        }
    }
}