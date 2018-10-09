#!/usr/bin/python
#encoding:utf-8

import telnetlib
import threading
import threading
import sys
import requests
import time

def so(url):
    for port in range(1,65536):
        try:
            t = threading.Thread(target=scan, args=(url, port, ))
            t.start()
        except:
            pass


def scan(url, port):
    try:
        #file = open('result.txt', 'w+')
        url2 = "http://"+url+":"+str(port)

        if port % 3 == 0 or port == 65535:
            print(url2)


        if port == 65535:
            time.sleep(2)
            print("\r\n\r\n")
            print("扫描完毕：".decode("utf-8").encode("gbk"))
            print("****************OK********************")

        reponse = requests.get(url2, timeout=3, headers=header)
        code = reponse.status_code

        if code == 200 or code == 302 or code == 404 or code == 403 or code == 500:
            print(url2+'--'+str(code)+'***************端口存活'.decode("utf-8").encode("gbk"))
            file = r'result.txt'

            with open(file, 'a+') as f:
                f.write(url2+'--'+str(code)+'\n')
                f.close()
            #file.write(url2+'--'+str(code)+'\r\n')
            urls.append(url2+'-----'+str(code))


    except:
        pass


if __name__ == '__main__':
    urls = []
    threads = []
    if sys.argv[1]:
        url = sys.argv[1]

        header = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://'+url,
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
        file1 = open('result.txt','w')
        file1.close()
        so(url)
        time.sleep(2)


