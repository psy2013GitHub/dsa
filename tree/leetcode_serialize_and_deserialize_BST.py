#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BST: binary search tree
import sys

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
                using pre-order
        :type root: TreeNode
        :rtype: str
        """
        res = []
        stack = [root, ]
        while len(stack) > 0:
            node = stack.pop()
            if node: res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
               idea: deserialize using lower bound and upper bound
               time complexity: each node will be corrected-visited once and error-visited once, so, O(2n)
        :type data: str
        :rtype: TreeNode
        """
        return self.deserialize_helper([data, ], [0, ], -sys.maxint, sys.maxint)

    def deserialize_helper(self, data_ptr, pos_ptr, lb, ub):
        curr_pos = pos_ptr[0]
        num = 0
        while curr_pos < len(data_ptr[0]) and data_ptr[0][curr_pos] != ',':
            num = num * 10 + int(data_ptr[0][curr_pos])
            curr_pos += 1
        if curr_pos == pos_ptr[0]: return None
        if num < lb or num > ub: return None # `error-visited` once here
        root = TreeNode(num) # `correct-visited` once here
        pos_ptr[0] = curr_pos + 1
        root.left = self.deserialize_helper(data_ptr, pos_ptr, lb, num)
        root.right = self.deserialize_helper(data_ptr, pos_ptr, num, ub)
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))