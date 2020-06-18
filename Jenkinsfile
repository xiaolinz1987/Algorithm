pipeline {

	agent any

	stages {

		stage('unit tests') {
			steps {
				sh 'python3 ./Python/tests/testutils.py -v'
				sh 'python3 ./Python/tests/testsorts.py -v'
				sh 'python3 ./Python/tests/testapps.py -v'
				sh 'python3 ./Python/tests/testprojects.py -v'
			}
		}
	}
}
