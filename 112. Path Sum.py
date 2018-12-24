# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        def dfs(node, sumtn, val):
            sumtn = sumtn + node.val
            print(sumtn)
            if((node.left == None) and (node.right == None)):
                if sumtn == val:
                    print("Hookla")
                    return True
            l = r = False
            if node.left != None:
                l = dfs(node.left, sumtn, val)
            if node.right != None:
                r = dfs(node.right, sumtn, val)
            
            return (l or r)
            
        return dfs(root, 0, sum)
        
