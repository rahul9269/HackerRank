class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None


class CreateBinary:
    def __init__(self):
        self.result = []
        pass
    
    def createTree(self):
        root = Node(15)
        root.left =  Node(10)
        root.right =  Node(20)
        root.left.left =  Node(8)
        root.left.left.left =  Node(6)
        root.left.right =  Node(12)
        root.left.right.left =  Node(11)
        root.right.right =  Node(25)
        root.right.left =  Node(17)
        root.right.right.right =  Node(27)
        root.right.left.left =  Node(16)
        return root
    
    def isLeaf(self,root):
        if (root.left == None and root.right == None):
            return True
        else:
            return False
    def preOrder(self,root):
        if root:
            self.result.append(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)
             
        return self.result
        
    def postOrder(self,root):
        if root:
            
            self.postOrder(root.left)
            self.postOrder(root.right)
            self.result.append(root.val)
        return self.result    
    
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            self.result.append(root.val)
            self.inOrder(root.right)
        return self.result
    def inOrderIterative(self,root):
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
                        print cur.val
                        cur = cur.right
                    else:
                        break
    
    def postOrderIterative(self,root):
        if root:
            stack =[]
            out = []
            stack.append(root)
            while stack:
                cur = stack.pop()
                out.append(cur)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            
            while out:
                print out.pop().val
                
     
cb = CreateBinary()
# print cb.inOrder(cb.createTree())
# print cb.postOrder(cb.createTree())
# cb.postOrderIterative(cb.createTree())