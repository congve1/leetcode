# 4的幂

## 描述

给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

**示例 1:**

    
    
    **输入:** 16
    **输出:** true
    

**示例 2:**

    
    
    **输入:** 5
    **输出:** false

**进阶：**  
你能不使用循环或者递归来完成本题吗？



# Power of Four

## Description



Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

**Example 1:**

    
    

    **Input:** 16

    **Output:** true

    

**Example 2:**

    
    

    **Input:** 5

    **Output:** false

**Follow up** : Could you solve it without loops/recursion?


**Tags:** Bit Manipulation

**Difficulty:** Easy

**思路:**
4的幂肯定是2的幂
首先先判断是不是2的幂
4的幂在二进制表达中有一个特点，就是只有1个1，且一定在奇数位上与0x55555555相与可以判断出1是否在奇数位上
