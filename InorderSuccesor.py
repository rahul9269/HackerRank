'''
Created on Jan 19, 2016

@author: Rahul
'''
from Node import *

def InorderSuccessor(root,k):
    b = 0
    if root:
        stack = []
        cur  = root
        while True:
            if(cur):
                stack.append(cur)
                cur = cur.left
            else:
                if stack:
                    cur = stack.pop()
                    if b:
                        return cur.val
                        break
                    if cur.val == k:
                        if cur.left == cur.right == None:
                            succ = stack.pop()
                            return succ.val
                            break
                        elif cur.left !=None and cur.right ==None:
                            succ = stack.pop()
                            return succ.val
                            break
                        elif cur.right !=None:
                            b = 1
                    cur = cur.right
                else:
                    break
    return None
if __name__ == '__main__':
    cb = CreateBinary()
    root= cb.createTree()
    k = 20
    print InorderSuccessor(root,k)