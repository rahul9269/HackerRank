'''
Created on Jan 13, 2016

@author: Rahul
'''

def check(str):
    i = 0
    ac = 0
    l = list(str)
    for c in l:
        if not c == 'b':
            l[i] = c
            i +=1
        if c == 'a':
            ac+=1
    len = i + ac
    
    print l
    while len >= 0:
        if l[len - 1] =='a':
            l[len -1] = 'aa'
        len -=1 

    print l
if __name__ == '__main__':
    pas = "sadsadabda"
    print check(pas)
