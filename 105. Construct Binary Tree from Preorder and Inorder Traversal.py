# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
                        
        def buildtree(preorder, inorder):
            if not inorder:
                return None
            
            root = TreeNode(preorder.popleft())
            split = inorder.index(root.val)
            root.left = buildtree(preorder, inorder[:split])
            root.right = buildtree(preorder, inorder[split+1:])
            
            return root
        
        return buildtree(deque(preorder), inorder)
