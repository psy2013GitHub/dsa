#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        recur unit:
                        root
                       /   \
                     left  right
                     / \    /  \
                   l.l l.r r.l r.r
            return max(root.val + ll + lr + rl + rr, left + right)
        """
        return self.helper(root, [0,], [0,])

    def helper(self, root, l, r):
        if not root:
            return
        ll, lr, rl, rr = [0,], [0,], [0,], [0,]
        l[0] = self.helper(root.left, ll, lr)
        r[0] = self.helper(root.right, rl, rr)
        return max(root.val + ll[0] + lr[0] + rl[0] + rr[0], l[0] + r[0])