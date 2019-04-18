# 杨辉三角

## 描述

给定一个非负整数  _numRows，_ 生成杨辉三角的前  _numRows  _行。

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

**示例:**

    
    
    **输入:** 5
    **输出:**
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]



# Pascal's Triangle

## Description



Given a non-negative integer  _numRows_ , generate the first _numRows_ of Pascal's triangle.

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)  
In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Example:**

    
    

    **Input:** 5

    **Output:**

    [

         [1],

        [1,1],

       [1,2,1],

      [1,3,3,1],

     [1,4,6,4,1]

    ]

    


**Tags:** Array

**Difficulty:** Easy

**思路:**
虽然这一算法非常简单，但用于构造杨辉三角的迭代方法可以归类为动态规划，因为我们需要基于前一行来构造每一行。
复杂度分析：
- 时间复杂度: $O(numrows^2)$
- 空间复杂度: $O(numrows^2)$
