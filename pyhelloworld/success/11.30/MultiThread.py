# -*- coding: utf-8 -*-
# (C) Guangcai Ren <renguangcai@jiaaocap.com>
# All rights reserved
# create time '2019/6/26 14:41'
import math
import random
import time
from concurrent.futures import ThreadPoolExecutor


def split_list():
    # 线程列表
    new_list = []
    count_list = []
    # 需要处理的数据
    _l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 每个线程处理的数据大小
    split_count = 2
    # 需要的线程个数
    times = math.ceil(len(_l) / split_count)
    count = 0
    for item in range(times):
        _list = _l[count: count + split_count]
        new_list.append(_list)
        count_list.append(count)
        count += split_count
    return new_list, count_list


def work(df, _list):
    """ 线程执行的任务，让程序随机sleep几秒

    :param df:
    :param _list:
    :return:
    """
    sleep_time = random.randint(1, 5)
    print(f'count is {df},sleep {sleep_time},list is {_list}')
    time.sleep(sleep_time)
    return sleep_time, df, _list


def use():
    pool = ThreadPoolExecutor(max_workers=5)
    new_list, count_list = split_list()
    # map返回一个迭代器，其中的回调函数的参数 最好是可以迭代的数据类型，如list；如果有 多个参数 则 多个参数的 数据长度相同；
    # 如： pool.map(work,[[1,2],[3,4]],[0,1]]) 中 [1,2]对应0 ；[3,4]对应1 ；其实内部执行的函数为 work([1,2],0) ; work([3,4],1)
    # map返回的结果 是 有序结果；是根据迭代函数执行顺序返回的结果

    # 使用map的优点是 每次调用回调函数的结果不用手动的放入结果list中
    results = pool.map(work, new_list, count_list)
    print(type(results))
    # 如下2行 会等待线程任务执行结束后 再执行其他代码
    for ret in results:
        print(ret)
    print('thread execute end!')

if __name__ == '__main__':
    use()