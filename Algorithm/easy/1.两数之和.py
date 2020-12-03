#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# dict { val : index}

        d = dict()
        for i, num in enumerate(nums): # get num
            if target - num in d:
                # return [i,d[target-num]] #! 先入dict的必定是之前的值
                return [d[target-num],i]
            else:
                d[num] = i




# @lc code=end

