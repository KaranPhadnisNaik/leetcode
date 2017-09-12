# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #empty root is symetric
        if not root:
            return True
        return self.findSymetry(root.left, root.right)

    def findSymetry(self, left,right):
        # check if left OR right are missing return none but if both are there and both are none
        # return true,
        if left == None or right == None:
            return left == right
        if (left.val == right.val):
            return self.findSymetry(left.left, right.right) & self.findSymetry(left.right,right.left)
        else:
            return False
