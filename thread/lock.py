import time, threading
#saving in bank
balance = 0

def change_it(n):
    global balance
    # save money before get it 
    balance = balance + n
    balance = balance - n
    print(balance)

def run_thread(n):
    for i in range(100):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance