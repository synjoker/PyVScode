#不使用Lock锁的例子
import logging
import threading
import time
logging.basicConfig(level=logging.INFO)
 
# 10 -> 100cups
cups = []
lock = threading.Lock()
 
 
def worker(lock:threading.Lock,task=100):
    while True:
        count = len(cups)
        time.sleep(0.1)
 
        if count >= task:
            break
 
        logging.info(count)
        cups.append(1)
        logging.info("{} make 1........ ".format(threading.current_thread().name))
    logging.info("{} ending=======".format(len(cups)))
 
for x in range(10):
    threading.Thread(target=worker,args=(lock,100)).start()