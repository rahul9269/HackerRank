'''
Created on Jan 18, 2016

@author: Rahul
Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()() 

Input:  ()(()))))
Output: 6
Explanation:  ()(()))

'''
def lvs(s):
    t = 0
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char ==')':
            if stack:
                stack.pop()
                t = t + 2
        else:
            pass
    return t    
if __name__ == '__main__':
    s = ")()())"
    print lvs(s)