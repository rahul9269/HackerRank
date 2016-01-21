'''
Created on Jan 10, 2016

@author: Rahul
'''
from Node import *
from copy import deepcopy
from numpy import Infinity


def find(root,data):
    stack =[]
    stack.append(root)
    while stack:
        n = stack.pop()
        if n.val == data:
            return n
        else:
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
    return None
        
def getParent(root,node):
    if root == node:
        return None
    stack = []
    stack.append(root)
    
    while stack:
        n = stack.pop()
        if n.left == node:
            return (n,"left")
        if n.right == node:
            return (n,"right")
        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)
    return None

    
def getMin(root):
    if root == None:
        return None
        
    stack = []
    min1 = 1000
    minnode = root
    stack.append(root)
    while stack:
        n = stack.pop()
        if n.val <= min1:
            min1 = n.val
            minnode = n
        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)
    
    return minnode 
        
        
        
def deleteNode(root,data):
    if root == None:
        return root
    current = find(root,data)
    if current:
        #case 1:leaf
        if current.left == None and current.right == None:
            parent,pos = getParent(root,current)
            if pos == "left":
                parent.left = None
            else:
                parent.right= None
            return root
        #case 2
        elif current.right == None:
                parent,pos = getParent(root,current)
                child = current.left
                if pos == "left":
                    parent.left = child
                else:
                    parent.right = child
                return root
        elif current.left == None:
                parent,pos = getParent(root,current)
                child = current.right
                if pos == "left":
                    parent.left = child
                else:
                    parent.right = child
                return root
        #case 3
        else:
            parent,pos = getParent(root,current)
            minnode = getMin(current.right)
            current.val = minnode.val
            current.right = deleteNode(current.right,minnode.val)
            return root
    else:
        return current        
if __name__ == '__main__':
    cb = CreateBinary()
    root = cb.createTree()
    root = deleteNode(root,23)
    
    if not root:
        print "element does not exist"
    else:
        print cb.inOrder(root)