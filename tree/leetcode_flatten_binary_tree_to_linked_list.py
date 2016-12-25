# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = list()
        prev_node = None
        stack.append(root)
        while len(stack) > 0:
            curr_node = stack.pop()
            if not curr_node: continue
            if prev_node:
                prev_node.right = curr_node
                prev_node.left = None
            stack.append(curr_node.right)
            stack.append(curr_node.left)
            prev_node = curr_node
        return
