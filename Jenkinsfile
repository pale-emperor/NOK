pipeline {
    agent {
       label "epyc-tempesta-test"
    }

    stages {
        stage('Get tempesta tests') {
            steps {
                sh 'rm -rf /home/tempesta/tempesta-test'
                sh 'git clone https://github.com/tempesta-tech/tempesta-test.git /home/tempesta/tempesta-test'
            }
        }
    }
}