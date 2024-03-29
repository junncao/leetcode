#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (31.90%)
# Likes:    273
# Dislikes: 0
# Total Accepted:    23.6K
# Total Submissions: 73.7K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=j=len(nums)-1
        while i>=1 and nums[i-1]>=nums[i] :
            i-=1
        if i==0:
            return nums.reverse()
        #定位到最后递减的位置
        while j>=0 and nums[j]<=nums[i-1]:
            j-=1
        nums[j],nums[i-1]=nums[i-1],nums[j]
        left=i
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1


        



