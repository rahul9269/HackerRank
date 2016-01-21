'''
Created on Jan 18, 2016

@author: Rahul
'''

def magicIndex(low,high,l):
    if high < 0 or low > len(l) - 1 or low > high:
        return -1  
    
    mid= (low + high)/2
    
    if l[mid] == mid:
        return mid
    leftindex = min(l[mid],mid -1)
    left = magicIndex(low, leftindex, l)
    if left > 0:
        return left
    rightindex = max(l[mid],mid + 1)
    right = magicIndex(rightindex, high, l)
    if right > 0:
        return right 
    
    return -1

if __name__ == '__main__':
    l = [-10,-5,1,2,2,7,7,7,9,12,13]
    print magicIndex(0,len(l)-1,l)
    