import threading, time

def worker(id):
    time.sleep(1)
    print('thread name = {} is {}'.format(threading.current_thread().name, id))

def threadmain():
    count = 1
    while True:
        if count == 6:
            t2 = threading.Thread(target=worker,name='t2', args=(count, ))
            t2.run()
            count += 1
            continue
        if count > 10:
            break
        time.sleep(0.5)
        count += 1
        print("thread name = {} is {}".format(threading.current_thread().name, id))
 
t1 = threading.Thread(target=threadmain, name="t1")
t1.start()
