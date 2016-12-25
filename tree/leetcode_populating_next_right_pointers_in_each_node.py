
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    # O(1) BFS by next pointer
    def connect(self, root):
        while root:
            curr_node = root
            while curr_node: # loop current level
                if curr_node.left:
                    curr_node.left.next = curr_node.right
                if curr_node.next:
                    if curr_node.right:
                        curr_node.right.next = curr_node.next.left
                curr_node = curr_node.next
            root = root.left # to next level