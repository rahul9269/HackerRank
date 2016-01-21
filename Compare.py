'''
Created on Sep 9, 2015

@author: Rahul
'''
import sys
def print_max(a=[]):
    global count
    max=a.pop()
    for item in a:
        if item > max:
            count = count + 1
            max=item
        else:
            count = count + 1
            pass
    print max


def print_min(b=[]):
    global count
    min= b.pop()
    for item in b:
        if item < min:
            count = count + 1
            min=item
        else:
            count = count + 1
            pass
    print min
    
if __name__ == '__main__':
    max =[]
    min=[]
    Arr=[0,34,23,7,13,13,131,111]
    count = 0
    i=0
    n= len(Arr)
    if n <2:
        print "Not a valid array"
        sys.exit()
        
    while i < n:
        if i+1 < n:
            if Arr[i] < Arr[i+1]:
                max.append(Arr[i+1])
                min.append(Arr[i])
                count = count + 1
            else:
                count = count + 1
                min.append(Arr[i+1])
                max.append(Arr[i])
            i = i + 2
        else:
            if Arr[i] > max[0]:
                count = count + 1
                max.append(Arr[i])
            else:
                count = count + 1
                min.append(Arr[i])
            i= i +2
                
    print_max(max)
    print_min(min)
    print "Total Number of comparisons done %d"%count


    
    