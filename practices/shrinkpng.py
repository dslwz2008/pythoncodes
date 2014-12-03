# -*-coding:utf-8-*-

import os
import os.path
import base64

import requests

import sys


key = "PFf5cne_akVBzjFobEnD4zeZ_v7KzSIM"
usage = '''只支持压缩png和jpg图片。
用法：python shrinkpng.py input.png 
或者：python shrinkong.py inputdir
请指定输出文件和输出文件！'''
postfix = 'shrunk'


def shunk_name(raw_name):
    dirname = os.path.dirname(raw_name)
    basename = os.path.basename(raw_name)
    return '/'.join([dirname, postfix, basename])


def shrink_pic(input_file, output_file):
    url = "https://api.tinypng.com/shrink"
    auth = base64.b64encode("api:" + key)
    headers = {"Authorization": "Basic %s" % auth}
    r1 = requests.post(url, data=open(input_file, 'rb'), headers=headers)
    if r1.status_code == 201:
        dirname = os.path.dirname(output_file)
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        # Compression was successful, retrieve output from Location header.
        target_url = r1.headers["location"]
        r2 = requests.get(target_url)
        if r2.status_code == 200:
            of = open(output_file, "wb")
            of.write(r2.content)
            print(output_file + " 压缩成功！")
        else:
            print('获取结果失败！')
    else:
        # Something went wrong! You can parse the JSON body for details.
        print("压缩失败！")


def shrink_dir(input_dir):
    for bn in os.listdir(input_dir):
        ext = bn.split('.')[-1]
        if ext.lower() == 'png' or ext.lower() == 'jpg':
            filename = '/'.join([input_dir, bn])
            shrink_pic(filename, shunk_name(filename))


if __name__ == '__main__':
    # test_params = ['shrinkpng.py', 'test/1.png']
    test_params = ['shrinkpng.py', 'D:/programs/workspace_python/pythoncodes/practices/test']
    sys.argv = test_params
    if len(sys.argv) == 1:
        print(usage)
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        if os.path.isfile(filename):
            basename = os.path.basename(filename)
            ext = basename.split('.')[-1]
            if ext.lower() == 'png' or ext.lower() == 'jpg':
                shrink_pic(filename, shunk_name(filename))
            else:
                print(usage)
        elif os.path.isdir(sys.argv[1]):
            shrink_dir(sys.argv[1])
        else:
            print('参数无效！')
            print(usage)
    else:
        print(usage)
