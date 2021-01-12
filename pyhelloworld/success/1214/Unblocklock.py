#非阻塞锁
import threading,logging,time
 
FORMAT = '%(asctime)s\t [%(threadName)s,%(thread)d] %(message)s'
logging.basicConfig(level=logging.INFO,format=FORMAT)
 
def worker(tasks):
    for task in tasks:
        time.sleep(0.01)
        if task.lock.acquire(False): #False非阻塞
            logging.info('{} {} begin to start'.format(threading.current_thread().name,task.name))
        else:
            logging.info('{} {} is working'.format(threading.current_thread().name,task.name))
 
class Task:
    def __init__(self,name):
        self.name = name
        self.lock = threading.Lock()
 
tasks = [Task('task={}'.format(t)) for t in range(5)]
 
for i in range(3):
    t = threading.Thread(target=worker,name='worker-{}'.format(i),args=(tasks,))
    t.start()