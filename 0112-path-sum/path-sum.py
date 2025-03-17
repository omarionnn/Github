# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, target):
            if not root:
                return False

            if not root.left and not root.right:
                if target == root.val:
                    return True

            target -= root.val
            return dfs(root.left, target) or dfs(root.right, target)

        return dfs(root, targetSum)
        