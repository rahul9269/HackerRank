'''
Created on Jan 11, 2016

@author: Rahul
'''

def merge(l,n):
    print "OP"
    if n == 0:
        return 0 
    print l
    for i in range(n):
        len1 = len(l[i])
        l.remove(l[i])
        return merge(l ,n-1) + len1

if __name__ == '__main__':
    l = ["kokoooo","grgt","qweqwe","tytrge","asd","vx"]
    
    
    print merge(l,len(l))