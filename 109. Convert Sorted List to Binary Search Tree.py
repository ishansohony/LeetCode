# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        while(head != None):
            array.append(head.val)
            head = head.next
            
        def maketree(array):
            if len(array) == 0:
                return None
            node = TreeNode(array[int(len(array)/2)])
            node.left = maketree(array[:int(len(array)/2)])
            node.right = maketree(array[int(len(array)/2)+1:])
            return node
        
        
        return maketree(array)
