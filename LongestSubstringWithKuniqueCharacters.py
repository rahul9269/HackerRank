'''
Created on Jan 18, 2016

@author: Rahul
"aabbcc", k = 1
Max substring can be any one from {"aa" , "bb" , "cc"}.
"aabbcc", k = 2
Max substring can be any one from {"aabb" , "bbcc"}.
"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.

"aaabbb", k = 3
There are only two unique characters, thus show error message.

'''
MAX_CHARS = 26
from __builtin__ import str

def valid(d,k):
    count = 0
    for e in d.values():
        if e != 0:
            count +=1
    
    return count <= k 

def getMaxString(s,k):
    d = {}
    for char in s:
        if char in d:
            d[char]+=1
        else:
            d[char] =1
    u = len(d)
    if k > u:
        return None
#     print d
    d ={}
    start = 0
    end = 0
    max = 1
    max_start = 0
    for i in range(0,len(s)):
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]] =1
        end = i
        print d
        while not valid(d,k):
            d[s[start]] -= 1
            start +=1 
    
    if end - start > max:
        max = end -start 
        max_start = start           
    
    
    print max_start
    print max
        
if __name__ == '__main__':
    str = "abaaaacfffffaabbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccc"
    k = 3
    print getMaxString(str,k)