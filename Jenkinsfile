pipeline {

	agent any

	stages {

		stage('unit tests of utils') {
			steps {
				sh 'python3 ./Python/tests/testutils.py -v'
			}
		}

		stage('unit tests of sorts') {
			steps {
				sh 'python3 ./Python/tests/testsorts.py -v'
			}
		}

		stage('unit tests of apps') {
			steps {
				sh 'python3 ./Python/tests/testapps.py -v'
			}
		}

		stage('unit tests of projects') {
			steps {
				sh 'python3 ./Python/test_projects/testbitmap.py'
				sh 'python3 ./Python/test_projects/testlrucache.py'
				sh 'python3 ./Python/test_projects/testastarsearch.py'
				sh 'python3 ./Python/test_projects/testredpackage.py'
			}
		}
	}
}
