# 格雷编码

## 描述

格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 _n_ ，打印其格雷编码序列。格雷编码序列必须以 0 开头。

**示例 1:**

    
    
    **输入:**  2
    **输出:**  [0,1,3,2]
    **解释:**
    00 - 0
    01 - 1
    11 - 3
    10 - 2
    
    对于给定的  _n_ ，其格雷编码序列并不唯一。
    例如，[0,2,3,1] 也是一个有效的格雷编码序列。
    
    00 - 0
    10 - 2
    11 - 3
    01 - 1

**示例  2:**

    
    
    **输入:**  0
    **输出:**  [0]
    **解释:** 我们定义格雷编码序列必须以 0 开头。
         给定编码总位数为 _n_ 的格雷编码序列，其长度为 2n。当 _n_ = 0 时，长度为 20 = 1。
         因此，当 _n_ = 0 时，其格雷编码序列为 [0]。
    



# Gray Code

## Description



The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer _n_ representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

**Example 1:**

    
    
    **Input:**  2
    **Output:**  [0,1,3,2]
    **Explanation:**
    00 - 0
    01 - 1
    11 - 3
    10 - 2
    
    For a given  _n_ , a gray code sequence may not be uniquely defined.
    For example, [0,2,3,1] is also a valid gray code sequence.
    
    00 - 0
    10 - 2
    11 - 3
    01 - 1
    

**Example 2:**

    
    
    **Input:**  0
    **Output:**  [0]
    **Explanation:** We define the gray code sequence to begin with 0.
                 A gray code sequence of _n_ has size = 2n, which for _n_ = 0 the size is 20 = 1.
                 Therefore, for _n_ = 0 the gray code sequence is [0].
    


**Tags:** Backtracking

**Difficulty:** Medium

**思路:**
