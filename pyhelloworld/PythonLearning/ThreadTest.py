# # 创建threading.Thraed对象
# import threading
# import time

# def tstart(arg):
#     time.sleep(0.5)
#     print("%s running...." % arg)

# if __name__ == '__main__':
#     t1 = threading.Thread(target=tstart, args=('This is thread 1',))
#     t2 = threading.Thread(target=tstart, args=('This is thread 2',))
#     t1.start()
#     t2.start()
#     print("This is main function")

# # 继承threading.Thraed对象，并重写run
# import threading
# import time

# class CustomThread(threading.Thread):
#     def __init__(self, thread_name):
#         # step 1: call base __init__ function
#         super(CustomThread, self).__init__(name=thread_name)
#         self._tname = thread_name

#     def run(self):
#         # step 2: overide run function
#         time.sleep(0.5)
#         print("This is %s running...." % self._tname)

# if __name__ == "__main__":
#     t1 = CustomThread("thread 1")
#     t2 = CustomThread("thread 2")
#     t1.start()
#     t2.start()
#     print("This is main function")

# join 多线程执行
import threading
import time

def tstart(arg):
    print("%s running....at: %s" % (arg,time.time()))
    time.sleep(1)
    print("%s is finished! at: %s" % (arg,time.time()))

if __name__ == '__main__':
    t1 = threading.Thread(target=tstart, args=('This is thread 1',))
    t1.start()
    # t1.join()   # 当前线程阻塞，等待t1线程执行完成
    print("This is main function at：%s" % time.time())