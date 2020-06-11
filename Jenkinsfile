pipeline {

	agent any

	stages {

		stage('compile utils') {
			steps {
				sh 'python3 ./Python/utils/__init__.py'
				sh 'python3 ./Python/utils/array.py'
				sh 'python3 ./Python/utils/heap.py'
				sh 'python3 ./Python/utils/linkedlist.py'
				sh 'python3 ./Python/utils/queue.py'
				sh 'python3 ./Python/utils/tree.py'
				sh 'python3 ./Python/utils/priorityqueue.py'
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
