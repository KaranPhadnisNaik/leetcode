# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return when you have No more nodes
        if not root:
            return 0
        # recursively call left trees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # get max left and right values for the subtrees of node and add one to include the current node
        return max(left,right)+1
