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
        if not root: return False
        return self.helper(root, 0, sum)

    def helper(self, root, prev_sum, target_sum):
        if not root: return False
        prev_sum += root.val
        if prev_sum == target_sum and self.is_leaf(root): return True
        return self.helper(root.left, prev_sum, target_sum) or self.helper(root.right, prev_sum, target_sum)

    def is_leaf(self, root):
        return not root.left and not root.right