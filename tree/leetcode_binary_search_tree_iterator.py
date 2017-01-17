# -*- encoding: utf8 -*-

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iter-pre-order(stack): space-complexity: O(h), time-complexity-next: O(h),  time-complexity-has-next: O(1)

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root:
            self.stack.append(root)
        self.last_node = None

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        val = None
        if self.hasNext():
            if not self.last_node or self.is_parent(self.stack[-1], self.last_node):
                self.untill_left()
            node = self.stack.pop()
            self.last_node = node
            val = node.val
        return val

    def untill_left(self):
        node = self.stack.pop()
        while node:
            if node.right:
                self.stack.append(node.right)
            self.stack.append(node)
            left = node.left
            node = left

    def is_parent(self, node1, node2):
        return node1 and node2 and (
        (node2.left and node2.left.val == node1.val) or (node2.right and node2.right.val == node1.val))

        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())