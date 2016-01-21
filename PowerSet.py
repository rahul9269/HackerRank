'''
Created on Jan 11, 2016

@author: Rahul
'''
import math

def powerset(str):
    l = len(str)
    counter = math.pow(2, l)
    
    for i in range(0,int(counter)):
        for j in range(l):
            if (i & 1<<j):
                print list(str)[j]
    
        print


if __name__ == '__main__':
    string = "abc"
    
    print powerset(string)
    