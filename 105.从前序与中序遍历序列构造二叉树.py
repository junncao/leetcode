#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (62.01%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    27.3K
# Total Submissions: 44K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder and preorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
        return None
# @lc code=end

