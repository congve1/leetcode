# 分糖果

## 描述

给定一个 **偶数** 长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果 **平均** 分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

**示例 1:**

    
    
    **输入:** candies = [1,1,2,2,3,3]
    **输出:** 3
    **解析:** 一共有三种种类的糖果，每一种都有两个。
         最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。
    

**示例 2 :**

    
    
    **输入:** candies = [1,1,2,3]
    **输出:** 2
    **解析:** 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。
    

**注意:**

  1. 数组的长度为[2, 10,000]，并且确定为偶数。
  2. 数组中数字的大小在范围[-100,000, 100,000]内。 



# Distribute Candies

## Description

Given an integer array with **even** length, where different numbers in this array represent different **kinds** of candies. Each number means one candy of the corresponding kind. You need to distribute these candies **equally** in number to brother and sister. Return the maximum number of **kinds** of candies the sister could gain.

**Example 1:**  

    
    
    **Input:** candies = [1,1,2,2,3,3]
    **Output:** 3
    **Explanation:**
    There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
    Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
    The sister has three different kinds of candies. 
    

**Example 2:**  

    
    
    **Input:** candies = [1,1,2,3]
    **Output:** 2
    **Explanation:** For example, the sister has candies [2,3] and the brother has candies [1,1]. 
    The sister has two different kinds of candies, the brother has only one kind of candies. 
    

**Note:**

  1. The length of the given array is in range [2, 10,000], and will be even.
  2. The number in given array is in range [-100,000, 100,000].


**Tags:** Hash Table

**Difficulty:** Easy

**思路:**
