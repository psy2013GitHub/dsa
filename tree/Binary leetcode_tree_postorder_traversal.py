#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        return self.iter_postorderTraversal(root)

    def iter_postorderTraversal(self, root):
        res = []
        stack = list()
        stack.append(root)
        curr_node = root
        while len(stack) > 0:
            if not self.is_parent(curr_node, stack[-1]): # if `not parent`, can't pop, push until left most leaf
                self.until_left(stack)
            curr_node = stack.pop()
            # print curr_node.val, [_.val for _ in stack]
            res.append(curr_node.val)
        return res

    def until_left(self, stack):
        node = stack[-1]
        while node:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                node = node.left
            else:
                node = node.right
        # stack.pop() # pop None

    def is_parent(self, node1, node2):
        return node2 and node1 and \
            ((node2.left and node2.left.val==node1.val) or (node2.right and node2.right.val==node1.val))