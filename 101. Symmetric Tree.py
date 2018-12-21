# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        def issame(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
            elif p.val == q.val:
                return (issame(p.left, q.right) and issame(p.right, q.left))
            else: return False
            
        return issame(root.left, root.right)
