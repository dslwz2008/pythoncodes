#-*-coding:utf-8-*-
__author__ = 'shenshen'

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                # temp = alist[i]
                # alist[i] = alist[i+1]
                # alist[i+1] = temp
                alist[i], alist[i+1] = alist[i+1], alist[i]

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

def insertionSort(alist):
   for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position - 1
        alist[position]=currentvalue

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        #如果前面还有的话，并且比当前值大，向前复制该项，直到找到合适的位置
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=currentvalue

def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition, sublistcount)
        print("After increments of size", sublistcount,
                   "The list is", alist)
        sublistcount = sublistcount // 2

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

if __name__ == '__main__':
    # alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # bubbleSort(alist)
    # print(alist)
    # alist=[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    # shortBubbleSort(alist)
    # print(alist)
    # alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    # shortBubbleSort(alist)
    # print(alist)
    # alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # insertionSort(alist)
    # print(alist)
    # alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # shellSort(alist)
    # print(alist)
    # alist = [54,26,93,17,77,31,44,55,20]
    # mergeSort(alist)
    # print(alist)
    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)

