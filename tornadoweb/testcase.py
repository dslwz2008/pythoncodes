# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import requests

def testupload():
    url = 'http://localhost:8080/upload'
    filename = 'C:/Users/Public/Pictures/Sample Pictures/test.jpg'
    files = {'image': open(filename, 'rb')}
    r = requests.post(url, files=files)
    print(r.json())

if __name__ == '__main__':
    testupload()