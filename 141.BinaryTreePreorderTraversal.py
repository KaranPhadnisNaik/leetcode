# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.final = []
        self.preOrder(root)
        return self.final

    def preOrder(self, root):
        if not root:
            return
        self.final.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
