import time, threading
#saving in bank
balance = 0

def change_it(n):
    global balance
    # save money before get it 
    balance = balance + n
    balance = balance - n
    balance = balance + n
    balance = balance - n
    balance = balance + n
    balance = balance - n
    print(balance)
    balance = balance + n
    balance = balance - n
    print(balance)
    balance = balance + n
    balance = balance - n
    print(balance)

def run_thread(n):
    for i in range(100):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t3 = threading.Thread(target=run_thread, args=(1,))
t4 = threading.Thread(target=run_thread, args=(2,))
t5 = threading.Thread(target=run_thread, args=(4,))
t6 = threading.Thread(target=run_thread, args=(9,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
print balance