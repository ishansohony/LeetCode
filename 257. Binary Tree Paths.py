# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        
        def dfs(node, path, path_list):
            if((node.left == None) and (node.right == None)):
                path = path + str(node.val)
                path_list.append(path)
            
            if node.left != None:
                pathl = path + str(node.val) + "->"
                dfs(node.left, ""+pathl, path_list)
            
            if node.right != None:
                pathr = path + str(node.val) + "->"
                dfs(node.right, ""+pathr, path_list)
            
            return path_list
        
        return dfs(root, "", [])
