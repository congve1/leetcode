# 132模式

## 描述

给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 a **i** , a **j** , a **k**  被定义为：当 **i** < **j** < **k** 时，a **i** < a **k** < a **j** 。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

**注意：** n 的值小于15000。

**示例1:**

    
    
    **输入:** [1, 2, 3, 4]
    
    **输出:** False
    
    **解释:** 序列中不存在132模式的子序列。
    

**示例 2:**

    
    
    **输入:** [3, 1, 4, 2]
    
    **输出:** True
    
    **解释:** 序列中有 1 个132模式的子序列： [1, 4, 2].
    

**示例 3:**

    
    
    **输入:** [-1, 3, 2, 0]
    
    **输出:** True
    
    **解释:** 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
    



# 132 Pattern

## Description



Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence a **i** , a **j** , a **k** such that **i** < **j** < **k** and a **i** < a **k** < a **j**. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

**Note:** n will be less than 15,000.

**Example 1:**  

    
    
    **Input:** [1, 2, 3, 4]
    
    **Output:** False
    
    **Explanation:** There is no 132 pattern in the sequence.
    

**Example 2:**  

    
    
    **Input:** [3, 1, 4, 2]
    
    **Output:** True
    
    **Explanation:** There is a 132 pattern in the sequence: [1, 4, 2].
    

**Example 3:**  

    
    
    **Input:** [-1, 3, 2, 0]
    
    **Output:** True
    
    **Explanation:** There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
    


**Tags:** Stack

**Difficulty:** Medium

**思路:**
