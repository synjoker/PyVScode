from multiprocessing import Process  
import os, time

def pstart(name):
    # time.sleep(0.1)
    print("Process name: %s, pid: %s "%(name, os.getpid()))

if __name__ == "__main__": 
    subproc = Process(target=pstart, args=('subprocess',))  
    subproc.start()  
    subproc.join()
    print("subprocess pid: %s"%subproc.pid)
    print("current process pid: %s" % os.getpid())

# 子进程程序
# import subprocess
# res = subprocess.Popen(['ping', 'www.cnblogs.com'], stdout=subprocess.PIPE).communicate()[0]
# print(res.decode('gbk')) # python 编辑器使用gbk显示 传输用uft-8

# pool池调用
# #coding=utf-8
# from multiprocessing import Pool
# import os, time, random

# def worker(msg):
#     print("%s开始执行,进程号为%d"%(msg, os.getpid()))
#     time.sleep(1)
#     print("%s执行完毕"%(msg))

# if __name__ == '__main__':
#     po = Pool(3)  # 定义一个进程池，最大进程数3
#     for i in range(10):
#         # Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
#         # 每次循环将会用空闲出来的子进程去调用目标
#         po.apply_async(worker, (i,))

#     print("----start----")
#     po.close()  # 关闭进程池，关闭后po不再接收新的请求
#     po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
#     print("-----end-----")

#     #coding=utf-8

# import os
# from multiprocessing import Pool


# def copyFileTask(name, oldFolderName, newFolderName):
#     # 完成copy一个文件的功能
#     fr = open(oldFolderName+"/"+name, 'rb+')
#     fw = open(newFolderName+"/"+name, 'wb+')

#     str = fr.read(1024 * 5)
#     while (str != ''):
#         fw.write(str)
#         str = fr.read(1024 * 5)

#     fr.close()
#     fw.close()


# def main():
#     # 获取要copy的文件夹名字
#     oldFolderName = raw_input('请输入文件夹名字：')
#     # 创建一个文件夹
#     newFolderName = oldFolderName+'-复件'.decode('utf-8').encode('gbk')
#     os.mkdir(newFolderName)

#     #获取old文件夹里面所有文件的名字
#     fileNames = os.listdir(oldFolderName)

#     #使用多进程的方式copy原文件夹所有内容到新的文件夹中
#     pool = Pool(5)
#     for name in fileNames:
#         pool.apply_async(copyFileTask, (name, oldFolderName, newFolderName))

#     pool.close()
#     pool.join()

# if __name__ == '__main__':
#     main()

# # 进程间queue通信-在pool进程池中
# from multiprocessing import Manager,Pool
# import time

# def write(q):
#     for i in ["A","B","C","D","E"]:
#         print("向队列中添加%s"%i)
#         q.put(i)
#         time.sleep(1)

# def read(q):
#     while not q.empty():
#         print("从队列中取出的值是%s"%q.get())
#         time.sleep(1)

# if __name__ == '__main__':
#     q = Manager().Queue()
#     pool = Pool()
#     pool.apply_async(write,args=(q,))
#     pool.apply_async(read,args=(q,))
#     # pool.apply(write,args=(q,))
#     # pool.apply(read,args=(q,))

#     pool.close()
#     pool.join()

#     print("数据通信完毕")

# Daemon守护线程
# from time import  ctime,sleep
# import threading

# def music(func):
#     #print(threading.current_thread())#线程对象
#     for i in range(2):
#         print('I was listening to %s. %s'%(func,ctime()))
#         sleep(2)
#         print('end listing %s'%ctime())
# def move(func):
#     #print(threading.current_thread())#线程对象
#     for i in range(2):
#         print('I was at the %s ! %s'%(func,ctime()))
#         sleep(3)
#         print('end moving %s' % ctime())

# threads=[]
# t1=threading.Thread(target=music,args=('星晴',))
# threads.append(t1)
# t2=threading.Thread(target=move,args=('正义联盟',))
# threads.append(t2)


# #Daemon(守护进程)将主线程设置为Daemon线程,它退出时,其它子线程会同时退出,不管是否执行完任务。
# if __name__=="__main__":
#     t2.setDaemon(True)#只守护t2，但不守护t1，t1会全部执行完，同时也会引发t2执行，但t2不会执行完，t1执行完，就退出
#     for t in threads:
#         #t.setDaemon(True)#（执行一次后就退出）
#         t.start()


#     #print(threading.current_thread())#线程对象
#     #print(threading.active_count())#线程对象的数量（默认会有一条主线程）
#     print('all over %s'%ctime())

# # 线程池
# import threading
# import time
# from time import  ctime,sleep
# def test(value1, value2=None):
#     print("%s threading is printed %s, %s"%(threading.current_thread().name, value1, value2))
#     time.sleep(2)
#     return 'finished'

# def test_result(future):
#     print(future.result())

# if __name__ == "__main__":
#     import numpy as np
#     from concurrent.futures import ThreadPoolExecutor
#     threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
#     for i in range(0,10):
#         future = threadPool.submit(test, i,i+1)
#         future.add_done_callback(test_result)
#         # print(future.result())

#     threadPool.shutdown(wait=True)
#     print('main finished')

# map函数返回值
from concurrent.futures import ThreadPoolExecutor
import requests

URLS = ['http://www.baidu.com', 'http://qq.com', 'http://sina.com']


def task(url, timeout=10):
    return requests.get(url, timeout=timeout)


pool = ThreadPoolExecutor(max_workers=3)
'''
  map()方法
  除了submit，Exectuor还为我们提供了map方法，这个方法返回一个map(func, *iterables)迭代器，迭代器中的回调执行返回的结果有序的
'''
results = pool.map(task, URLS)
for result in results:
    # print('{0},{1}'.format(result.url,len(result.content)))
    print('%s,%s' % (result.url, len(result.content)))