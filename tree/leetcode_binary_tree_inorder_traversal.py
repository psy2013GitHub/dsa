#-*- encoding: utf8 -*-

# `preorder`: root -> left-tree -> right-tree
# `inorder`: left-tree -> root -> right-tree
# `after-order`: left-tree, right-tree, root

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root, recur=True):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if recur:
            res = []
            self.recur_inorder(root, res)
            return res
        return self.iter_inorder(root)

    def recur_inorder(self, root, res):
        if not root:
            return
        self.recur_inorder(root.left, res)
        res.append(root.val)
        self.recur_inorder(root.right, res)

    def iter_inorder(self, root):
        '''
        :param root:
        :return:
        '''
        res = []
        stack = []
        if not root: return []
        stack.append(root)
        curr_node = None
        while len(stack) > 0:
            if self.is_parent(stack[-1], curr_node):
                self.until_left(stack)
            curr_node = stack[-1]
            res.append(curr_node.val)
        return res

    def is_parent(self, node1, node2):
        return node1 and node2 and \
               ((node2.left and node2.left.val==node1.val) or (node2.right and node2.right.val==node1.val))

    def until_left(self, stack):
        curr_node = stack.pop()
        while curr_node:
            if curr_node.right:
                stack.append(curr_node.right)
            stack.append(curr_node)
            if curr_node.left:
                stack.append(curr_node.left)
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right