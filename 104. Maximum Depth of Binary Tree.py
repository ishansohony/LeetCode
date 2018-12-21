# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node, count):
            if (node == None):
                return count
            else:
                count += 1
                return max(dfs(node.left, count), dfs(node.right, count))
                
                
        return dfs(root, 0)
        
