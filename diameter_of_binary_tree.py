# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self._max = 0
        
        def get_diameter(root):
            if not root:
                return 0
            L = get_diameter(root.left)
            R = get_diameter(root.right)
            self._max = max(self._max, L+R)
            return max(L, R)+1
        get_diameter(root)
        
        return self._max