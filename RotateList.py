'''
Created on Jan 12, 2016

@author: Rahul
'''

a = [2,3,9,5,4,6,7,8]
k = 3
counter = len(a) - k
for i in range(0,len(a)-k+1):
    temp = a[i]
    a[i] = a[counter]
    a[counter] = temp
    
    counter = counter + 1
    if counter == len(a):
        counter = len(a) - k
    print a