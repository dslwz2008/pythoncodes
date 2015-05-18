# -*-coding:utf-8-*-
# Author: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

# usage : python listds.py d:/data/ result.txt

import arcpy
import sys

def listds(dir):
    arcpy.env.workspace = dir
    return arcpy.ListDatasets()

def write2file(dslist, filename):
    with open(filename, 'w') as fp:
        for ds in dslist:
            fp.write(ds + '\n')

def main(dir, filename):
    write2file(listds(dir), filename)

if __name__ == '__main__':
    # dir = 'd:/data/'
    # filename = 'result.txt'
    dir = sys.argv[1]
    filename = sys.argv[2]
    main(dir, filename)