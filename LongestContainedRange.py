'''
Created on Jan 12, 2016

@author: Rahul
'''

if __name__ == '__main__':
    a = [10,5,3,11,6,100,4]
    d = {}
    for e in a:
        d[e] = 1
    maxset = 1    
    for i in range(len(a)):
        if a[i] in d:
            element = a[i]
            d.pop(a[i])
            set = 1
            while True:
                if element - 1 in d:
                    d.pop(element - 1)
                    set +=1
                    element = element - 1
                else:
                    break
            element = a[i]
            while True:
                if element + 1 in d:
                    d.pop(element + 1)
                    set +=1
                    element = element + 1
                else:
                    break
        if set > maxset:
            maxset = set
    print maxset