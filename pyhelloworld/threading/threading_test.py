'''
异步调用方式：
    缺点：存在耦合
    优点：速度快
'''
from concurrent.futures import ProcessPoolExecutor
import time, os
import requests
 
 
def get(url):
    print('%s GET %s' % (os.getpid(), url))
    time.sleep(3)
    response = requests.get(url)
    if response.status_code == 200:
        res = response.text
    else:
        res = '下载失败'
    parse(res)
 
 
def parse(res):
    time.sleep(1)
    print('%s 解析结果为%s' % (os.getpid(), len(res)))
 
 
if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.sina.com.cn',
        'https://www.tmall.com',
        'https://www.jd.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://www.baidu.com',
        'https://www.baidu.com',
        'https://www.baidu.com',
 
    ]
 
    p = ProcessPoolExecutor(9)
    start = time.time()
    for url in urls:
        future = p.submit(get, url)
    p.shutdown(wait=True)
 
    print('完成时间', time.time() - start)
 
'''
11980 GET https://www.baidu.com
15308 GET https://www.sina.com.cn
14828 GET https://www.tmall.com
11176 GET https://www.jd.com
14792 GET https://www.python.org
14764 GET https://www.openstack.org
11096 GET https://www.baidu.com
13708 GET https://www.baidu.com
2080 GET https://www.baidu.com
14828 解析结果为233353
11176 解析结果为108569
11980 解析结果为2443
15308 解析结果为569124
11096 解析结果为2443
13708 解析结果为2443
2080 解析结果为2443
14764 解析结果为65099
14792 解析结果为48821
完成时间 7.404443979263306
'''