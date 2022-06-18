pipeline {
    environment {
        TEMPESTA_PATH = "/home/tempesta/tempesta-test"
    }

    agent {
       label "tempesta-test"
    }

    stages {
        stage('Set buildName and cleanWS'){
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        currentBuild.displayName = "PR-${ghprbPullId}"
                    }
                    cleanWs()
                    sh 'rm -rf /root/tempesta'
                    sh 'ls ${TEMPESTA_PATH}'
                    sh 'echo ${TEMPESTA_PATH}'
                }
            }
        }

        stage('Build tempesta-fw') {
            steps {
                sh 'cp -r . /root/tempesta'
                dir("/root/tempesta"){
                    sh 'make'
                }
            }
        }

        stage('Checkout tempesta-tests') {
            steps {
                sh 'rm -rf ${TEMPESTA_PATH}'
                sh 'git clone https://github.com/tempesta-tech/tempesta-test.git ${TEMPESTA_PATH}'
            }
        }

        stage('Run tests') {
            steps {
                dir('${TEMPESTA_PATH}'){
                    sh './run_tests.py'
                }
            }
        }

    }
}
