# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree 
# were swapped by mistake. Recover the tree without changing its structure.

#Solution => inorder traversal of BST should gives a sorted array in ascending order.
#  then find the 2 swapped elements in that array
#  then go into a new traversal changing the swapped elements 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root: TreeNode) -> List[int]:
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right) if root else []

    def inOrderAndSwap(self, root: TreeNode, swapped: List[int]) -> None:
        if not root:
            return
        if root.val == swapped[0]:
            root.val = swapped[1]
        elif root.val == swapped[1]:
            root.val = swapped[0]
        self.inOrderAndSwap(root.left, swapped)
        self.inOrderAndSwap(root.right, swapped)
    
    def findTwoSwapped(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = y = None # Initialize x and y as a value that cannot be the value of a node.
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                y = nums[i + 1]
                # first swap occurrence
                if x is None:     
                    x = nums[i]
                # second swap occurrence
                else:           
                    break
        return [x, y]
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nums = self.inOrder(root)
        print(nums)
        swapped = self.findTwoSwapped(nums)
        print(swapped)
        self.inOrderAndSwap(root, swapped)
        
