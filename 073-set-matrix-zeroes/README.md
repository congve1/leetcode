# 矩阵置零

## 描述

给定一个  _m_ x _n_ 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用 **[原地](http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)** 算法 **。**

**示例  1:**

    
    
    **输入:** 
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    **输出:** 
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
    

**示例  2:**

    
    
    **输入:** 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    **输出:** 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]

**进阶:**

  * 一个直接的解决方案是使用  O( _m_ _n_ ) 的额外空间，但这并不是一个好的解决方案。
  * 一个简单的改进方案是使用 O( _m_  +  _n_ ) 的额外空间，但这仍然不是最好的解决方案。
  * 你能想出一个常数空间的解决方案吗？



# Set Matrix Zeroes

## Description



Given a _m_ x _n_ matrix, if an element is 0, set its entire row and column to 0. Do it [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm).

**Example 1:**

    
    
    **Input:** 
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    **Output:** 
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
    

**Example 2:**

    
    
    **Input:** 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    **Output:** 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
    

**Follow up:**

  * A straight forward solution using O( _m_ _n_ ) space is probably a bad idea.
  * A simple improvement uses O( _m_ \+ _n_ ) space, but still not the best solution.
  * Could you devise a constant space solution?


**Tags:** Array

**Difficulty:** Medium

**思路:**
