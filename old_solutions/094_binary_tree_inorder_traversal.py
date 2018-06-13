"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # idea: iterage every point
        if root == None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
    def initiate_BT(self, list):
        if list == None:
            return None
        if len(list) == 0:
            return None
        else: 
            root = TreeNode(list[0])
            if len(list) > 1: 
                if list[1] != None:
                    root.left = self.initiate_BT(list[1])
            else:
                root.left = None
            if len(list) > 2: 
                if list[2] != None:
                    root.right = self.initiate_BT(list[2])
            else:
                root.right = None
            return root
        
list = [1,None,[2,[3]]]
solution = Solution()
root = solution.initiate_BT(list)
print solution.inorderTraversal(root)
