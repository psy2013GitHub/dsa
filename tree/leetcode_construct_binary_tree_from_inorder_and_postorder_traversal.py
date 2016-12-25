#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(postorder[-1])
        root.right = TreeNode(postorder[-2])

    def helper(self, parent, inorder, postorder):
        root = TreeNode(postorder[-1])
        root.right = TreeNode(postorder[-2])
