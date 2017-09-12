# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # preorder traversal start with node then left then right
        if not t1 and not t2:
            return None
        # for the current node compute sum based on whether t1 or t2 exist
        t1val = t1.val if t1 else 0
        t2val = t2.val if t2 else 0
        tree = TreeNode(t1val+t2val)
        # get all the values in left trees. if that subtree doesnt exist set the pointer value to None
        tree.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        # get all the values in right trees. if that subtree doesnt exist set the pointer value to None
        tree.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return tree
