'''
Created on Jan 11, 2016

@author: Rahul
'''
from Node import *
from copy import deepcopy

L = 1
R = 0
def getmirror(root):
    if root == None:
        return None
    
    mroot = Node(root.val)
    queue = []
    queue.append((mroot,root.left,L))
    queue.append((mroot,root.right,R))
    while queue:
        mrt,n1,D = queue.pop(0)
        mnode = Node(n1.val)
        if D:
            mrt.right = mnode
        else:
            mrt.left = mnode
        
        if n1.left:
            queue.append((mnode,n1.left,L))
        if n1.right:
            queue.append((mnode,n1.right,R))
    
    return mroot        
        
    
    
    

if __name__ == '__main__':
    cb = CreateBinary()
    root = cb.createTree()
    mirror = getmirror(root)
    print cb.inOrder(mirror)