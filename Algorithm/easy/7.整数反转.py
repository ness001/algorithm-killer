#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (34.78%)
# Likes:    2384
# Dislikes: 0
# Total Accepted:    525.8K
# Total Submissions: 1.5M
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # --- #
        # 1. tackle for positive and negative
        # 2. x bit int boundary

        # --- #

        res = 0
        flag = -1 if x<0 else 1 # -123%10 = 7
        # 1<<31 -1 , bigest for 32 bit , and 1<<31 for smallest 
        boundary = (1<<31) -1 if x > 0 else (1<<31)
        x *= flag
        while(x):
            # ans*10未溢出时, ans*10个位为0, x%10的取值范围是0~9, 故ans*10 + x%10一定没有进位, 故不会溢出。# 存疑 # only for java
            # if ((x*10)%10) != 0:
            #     return 0
            res = x%10 + 10*res
            x = x//10
        return res*flag if res< boundary else 0


s=Solution()
s.reverse(-123)
pass
# @lc code=end

