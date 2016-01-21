'''
Created on Jan 12, 2016

@author: Rahul
'''
from Node import CreateBinary

MIN = 100000
MAX = -100000

def largetbst(root):
        if root == None:
            return (True,0,MIN,MAX)
        
        isbst = True
        size =0
        
        lbst,lsize,lmin,lmax = largetbst(root.left)
        rbst,rsize,rmin,rmax = largetbst(root.right)
        print root.val
        if (not lbst) or (not rbst) or (root.val < lmax) or (root.val > rmin):
            return (False,max(lsize,rsize),MIN,MAX)
        size = lsize + rsize + 1
        if not root.left == None:
            MIN = lmin 
        else:
            MIN =root.val;
        
        if not root.right == None:
            MAX = rmax
        else:
            MAX = root.val
            
        return (isbst,size,MIN,MAX)
        
        
    
if __name__ == '__main__':
    cb = CreateBinary()
    root = cb.createTree()
    
    print largetbst(root)