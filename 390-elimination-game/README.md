# 消除游戏

## 描述

给定一个从1 到 n 排序的整数列表。  
首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。  
第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。  
我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。  
返回长度为 n 的列表中，最后剩下的数字。

**示例：**

    
    
    **输入:**
    n = 9,
    _1_ 2 _3_ 4 _5_ 6 _7_ 8 _9_
    2 _4_ 6 _8_
    _2_ 6
    6
    
    **输出:**
    6



# Elimination Game

## Description



There is a list of sorted integers from 1 to _n_. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length _n_.

**Example:**

    
    
    Input:
    n = 9,
    _1_ 2 _3_ 4 _5_ 6 _7_ 8 _9_
    2 _4_ 6 _8_
    _2_ 6
    6
    
    Output:
    6
    


**Tags:** 

**Difficulty:** Medium

**思路:**
