#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] æå¤§å­åºå
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.07%)
# Total Accepted:    48.9K
# Total Submissions: 110.8K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# ç»å®ä¸ä¸ªæ´æ°æ°ç» numsÂ ï¼æ¾å°ä¸ä¸ªå·ææå¤§åçè¿ç»­å­æ°ç»ï¼å­æ°ç»æå°åå«ä¸ä¸ªåç´ ï¼ï¼è¿åå¶æå¤§åã
# 
# ç¤ºä¾:
# 
# è¾å¥: [-2,1,-3,4,-1,2,1,-5,4],
# è¾åº: 6
# è§£é:Â è¿ç»­å­æ°ç»Â [4,-1,2,1] çåæå¤§ï¼ä¸ºÂ 6ã
# 
# 
# è¿é¶:
# 
# å¦æä½ å·²ç»å®ç°å¤æåº¦ä¸º O(n) çè§£æ³ï¼å°è¯ä½¿ç¨æ´ä¸ºç²¾å¦çåæ²»æ³æ±è§£ã
# 
#
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -sys.maxsize - 1
        num_sum = 0
        for num in nums:
            num_sum = max((num_sum+num, num))
            res = max((num_sum, res))
        return res


