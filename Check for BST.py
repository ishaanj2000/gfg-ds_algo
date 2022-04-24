      def isBST(self, root):
        
        def bst(root, maxi, mini):
            if root == None:
                return True
            
            if root.data > maxi or root.data< mini:
                return False
                
            return bst(root.left, root.data, mini) and bst(root.right, maxi, root.data)
            
        return bst(root, sys.maxsize, -1* sys.maxsize)
