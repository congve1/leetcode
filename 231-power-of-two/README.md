# 2的幂

## 描述

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

**示例  1:**

    
    
    **输入:** 1
    **输出:** true
    **解释:** 20 = 1

**示例 2:**

    
    
    **输入:** 16
    **输出:** true
    **解释:** 24 = 16

**示例 3:**

    
    
    **输入:** 218
    **输出:** false



# Power of Two

## Description



Given an integer, write a function to determine if it is a power of two.

**Example 1:**

    
    

    **Input:** 1

    **Output:** true 

    **Explanation:** 20 = 1

    

**Example 2:**

    
    

    **Input:** 16

    **Output:** true

    **Explanation:** 24 = 16

**Example 3:**

    
    

    **Input:** 218

    **Output:** false


**Tags:** Bit Manipulation, Math

**Difficulty:** Easy

**思路:**
2的幂的二进制有一个特点，就是只有一个位是1
如果n 与 (n-1)==0,则说明，数字的二进制表达中只有一个1