# 递增的三元子序列

## 描述

给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

> 如果存在这样的  _i, j, k,  _ 且满足 0 ≤ _i_ < _j_ < _k_ ≤ _n_ -1，  
>  使得  _arr[i]_ < _arr[j]_ < _arr[k]_ ，返回 true ; 否则返回 false 。

**说明:** 要求算法的时间复杂度为 O( _n_ )，空间复杂度为 O( _1_ ) 。

**示例 1:**

    
    
    **输入:** [1,2,3,4,5]
    **输出:** true
    

**示例 2:**

    
    
    **输入:** [5,4,3,2,1]
    **输出:** false



# Increasing Triplet Subsequence

## Description



Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

> Return true if there exists _i, j, k_  
>  such that _arr[i]_ < _arr[j]_ < _arr[k]_ given 0 ≤ _i_ < _j_ < _k_ ≤ _n_ -1 else return false.

**Note:** Your algorithm should run in O( _n_ ) time complexity and O( _1_ ) space complexity.

**Example 1:**

    
    
    **Input:** [1,2,3,4,5]
    **Output:** true
    

**Example 2:**

    
    
    **Input:** [5,4,3,2,1]
    **Output:** false
    


**Tags:** 

**Difficulty:** Medium

**思路:**
