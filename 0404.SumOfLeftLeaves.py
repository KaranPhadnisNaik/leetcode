# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # if current node's left node is a terminal node, add that terminal node's value
        # to the remainder of the right subtree
        if  root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        # check the right and left subtrees
        return  self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


        
