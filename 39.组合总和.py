#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (66.71%)
# Likes:    376
# Dislikes: 0
# Total Accepted:    35.3K
# Total Submissions: 52.9K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#
class Solution(object):
    def combinationSum(self, candidates, target):
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def backward(nums, target,index,selected):

            if target<0:return 
            if target==0:
                res.append(selected)
                return 
            for i in xrange(index,len(nums)):
                if nums[i]>target:break
                backward(nums,target-nums[i],i,selected+[nums[i]])
        candidates.sort()
        backward(candidates,target,0,[])
        return res

