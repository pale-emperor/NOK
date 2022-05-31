pipeline {
    agent {
       label "epyc-tempesta-test"
    }

    stages {
        stage('tempesta-fw build') {
            steps {
                sh 'rm -rf /root/tempesta'
                sh 'git clone https://github.com/tempesta-tech/tempesta.git'
                sh 'ls -a'
                // sh 'make'
                // sh 'mv'
            }
        }

        stage('Get tempesta tests') {
            steps {
                sh 'rm -rf /home/tempesta/tempesta-test'
                sh 'git clone https://github.com/tempesta-tech/tempesta-test.git /home/tempesta/tempesta-test'
            }
        }
    }
}