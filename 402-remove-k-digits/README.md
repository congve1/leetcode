# 移掉K位数字

## 描述

给定一个以字符串表示的非负整数  _num_ ，移除这个数中的 _k_ 位数字，使得剩下的数字最小。

**注意:**

  * _num_ 的长度小于 10002 且 ≥ _k。_
  * _num_ 不会包含任何前导零。

**示例 1 :**

    
    
    输入: num = "1432219", k = 3
    输出: "1219"
    解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
    

**示例 2 :**

    
    
    输入: num = "10200", k = 1
    输出: "200"
    解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
    

示例 **3 :**

    
    
    输入: num = "10", k = 2
    输出: "0"
    解释: 从原数字移除所有的数字，剩余为空就是0。
    



# Remove K Digits

## Description



Given a non-negative integer _num_ represented as a string, remove _k_ digits from the number so that the new number is the smallest possible.

**Note:**  

  * The length of _num_ is less than 10002 and will be ≥ _k_.
  * The given _num_ does not contain any leading zero.

**

**Example 1:**

    
    
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    

**Example 2:**

    
    
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
    

**Example 3:**

    
    
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.
    


**Tags:** Stack, Greedy

**Difficulty:** Medium

**思路:**
