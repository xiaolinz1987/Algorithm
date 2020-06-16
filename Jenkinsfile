pipeline {

	agent any

	stages {

		stage('unit test of utils') {
			steps {
				sh 'python3 ./Python/test_utils/testarray.py'
				sh 'python3 ./Python/test_utils/testheap.py'
				sh 'python3 ./Python/test_utils/testlinkedlist.py'
				sh 'python3 ./Python/test_utils/testqueue.py'
				sh 'python3 ./Python/test_utils/testtree.py'
				sh 'python3 ./Python/test_utils/testpriorityqueue.py'
			}
		}

		stage('compile sorts') {
			steps {
				sh 'python3 ./Python/sorts/bubblesort.py'
				sh 'python3 ./Python/sorts/bucketsort.py'
				sh 'python3 ./Python/sorts/cocktailsort.py'
				sh 'python3 ./Python/sorts/quicksort.py'
				sh 'python3 ./Python/sorts/countsort.py'
				sh 'python3 ./Python/sorts/heapsort.py'
			}
		}

		stage('compile apps') {
			steps {
				sh 'python3 ./Python/apps/bestgoldmining.py'
				sh 'python3 ./Python/apps/cyclelist.py'
				sh 'python3 ./Python/apps/dictionarysort.py'
				sh 'python3 ./Python/apps/greatestcommondivisor.py'
				sh 'python3 ./Python/apps/greatestsorteddistance.py'
				sh 'python3 ./Python/apps/lostnumber.py'
				sh 'python3 ./Python/apps/mediansortedarrays.py'
				sh 'python3 ./Python/apps/minstack.py'
				sh 'python3 ./Python/apps/removekdigits.py'
				sh 'python3 ./Python/apps/stackqueue.py'
			}
		}

		stage('compile projects') {
			steps {
				sh 'python3 ./Python/projects/bitmap.py'
				sh 'python3 ./Python/projects/lcucache.py'
				sh 'python3 ./Python/projects/astarsearch.py'
				sh 'python3 ./Python/projects/redpackage.py'
			}
		}
	}
}
