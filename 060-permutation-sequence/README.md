# 第k个排列

## 描述

给出集合 `[1,2,3,…, _n_ ]`，其所有元素共有  _n_! 种排列。

按大小顺序列出所有排列情况，并一一标记，当  _n_ = 3 时, 所有排列如下：

  1. `"123"`
  2. `"132"`
  3. `"213"`
  4. `"231"`
  5. `"312"`
  6. `"321"`

给定  _n_ 和  _k_ ，返回第  _k_  个排列。

**说明：**

  * 给定 _n_  的范围是 [1, 9]。
  * 给定 _k  _的范围是[1,   _n_!]。

**示例  1:**

    
    
    **输入:** n = 3, k = 3
    **输出:** "213"
    

**示例  2:**

    
    
    **输入:** n = 4, k = 9
    **输出:** "2314"
    



# Permutation Sequence

## Description



The set `[1,2,3,..., _n_ ]` contains a total of _n_! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for _n_ = 3:

  1. `"123"`
  2. `"132"`
  3. `"213"`
  4. `"231"`
  5. `"312"`
  6. `"321"`

Given _n_ and _k_ , return the _k_ th permutation sequence.

**Note:**

  * Given _n_ will be between 1 and 9 inclusive.
  * Given  _k_  will be between 1 and _n_! inclusive.

**Example 1:**

    
    
    **Input:** n = 3, k = 3
    **Output:** "213"
    

**Example 2:**

    
    
    **Input:** n = 4, k = 9
    **Output:** "2314"
    


**Tags:** Math, Backtracking

**Difficulty:** Medium

**思路:**
