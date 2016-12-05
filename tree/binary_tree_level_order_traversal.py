#-*- encoding: utf8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
            bfs
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: # corner case
            return []
        res = []
        self.helper([root,], res)
        return res

    def helper(self, curr_nodes, res):

        if not curr_nodes:
            return

        children = []
        if len(curr_nodes) > 0:
            tmp = []
            for node in curr_nodes:
                if not node: continue
                tmp.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            res.append(tmp)

        if len(children) > 0:
            self.helper(children, res)

if __name__ == '__main__':
    pass