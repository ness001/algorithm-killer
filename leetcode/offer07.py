# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder.pop(0))
        idx=inorder.index(root.val)
        left_nodes=inorder[:idx]
        right_nodes=inorder[idx+1:]

        root.left=self.buildTree(preorder,left_nodes)
        root.right=self.buildTree(preorder,right_nodes)

        return root

s=Solution()
root=s.buildTree([3,9,20,15,7],[9,3,15,20,7])
a=1