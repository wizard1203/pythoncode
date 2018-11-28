# multiprocessing.py
import os
import time
while True:
	time.sleep(3)
	print('Process (%s) start...'% os.getpid())
	time.sleep(3)
	pid = os.fork()
	if pid==0:
		time.sleep(3)
		print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
	else:
		time.sleep(3)
		print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
