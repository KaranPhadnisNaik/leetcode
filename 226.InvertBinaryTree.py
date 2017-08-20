# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # we can try using DFS recrusively
        if not root:
            return root
        # from the root of the tree down flip the node's left and right subtrees
        root.left, root.right  = root.right, root.left
        # recursively call the left node then right node
        # Note: it does not matter whether you chose one or the other first
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
