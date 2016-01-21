'''
Created on Jan 10, 2016

@author: Rahul
'''
import heapq
from _heapq import heappush, heappop
if __name__ == '__main__':
    x = [1,0,3,5,2,0,1]
    
    minh = []
    maxh = []
    maxe = 0
    equal = 0
    for e in x:
        
        if equal == 0:
            heappush(minh,e)
            mine = heappop(minh)
            heappush(minh,mine)
            print mine 
            equal = 1
        else:
            heappush(minh,e)
            temp = heappop(minh)
            heappush(maxh,-temp)
            mine = heappop(minh)
            heappush(minh,mine)
            maxe = -1 * heappop(maxh)
            heappush(maxh,-maxe)
            median = float(maxe + mine) / 2
            equal = 0
            print median