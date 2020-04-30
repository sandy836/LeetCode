# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.dfs(root, arr, 0)
    
    def dfs(self, root, arr, depth):
        if not root or depth>=len(arr) or arr[depth] != root.val:
            return False
        if not root.left and not root.right:
            if depth + 1 == len(arr):
                return True
        return self.dfs(root.left, arr, depth+1) or self.dfs(root.right, arr, depth+1)