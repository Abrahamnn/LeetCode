# 题目：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数
使用内置函数  enumerate 比较好
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1+1:]):
                if num1 + num2 == target:
                    return [index1, index1+index2+1]
