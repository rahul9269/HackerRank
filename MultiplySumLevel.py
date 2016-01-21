'''
Created on Jan 8, 2016

@author: Rahul
'''
from Node import *

class MultiplySumLevel:
    
    def getLevelSum(self,root):
        cb = CreateBinary()
        result = 1
        stack = []
        stack.append(root)
        
        while stack:
            f = False
            sum  = 0
            size = len(stack)            
            while size > 0 :
                node = stack.pop(0)
                print node.val
                if cb.isLeaf(node):
                    f = True
                    sum = sum +  node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

                
                size -=1
            if f:
                result = result * sum    
        return result
if __name__ == '__main__':
    
    cb = CreateBinary()
    root = cb.createTree()
    ms= MultiplySumLevel()
    print ms.getLevelSum(root)
    