# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self._sum = -float('inf')
        def helper(root):
            if not root:
                return 0
            lsum = max(0, helper(root.left))
            rsum = max(0, helper(root.right))
            self._sum = max(self._sum, lsum+rsum+root.val)
            return root.val + max(lsum, rsum)
        helper(root)
        return self._sum