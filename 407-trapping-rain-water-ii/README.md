# 接雨水 II

## 描述

给定一个 `m x n` 的矩阵，其中的值均为正整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。



**说明:**

_m  _和 _n  _都是小于110的整数。每一个单位的高度都大于0 且小于 20000。



**示例：**

    
    
    给出如下 3x6 的高度图:
    [
      [1,4,3,1,3,2],
      [3,2,1,3,2,4],
      [2,3,3,2,3,1]
    ]
    
    返回 4。
    

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/rainwater_empty.png)

如上图所示，这是下雨前的高度图`[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]` 的状态。



![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/rainwater_fill.png)

下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。



# Trapping Rain Water II

## Description



Given an `m x n` matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.



**Note:**

Both _m_ and _n_ are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.



**Example:**

    
    
    Given the following 3x6 height map:
    [
      [1,4,3,1,3,2],
      [3,2,1,3,2,4],
      [2,3,3,2,3,1]
    ]
    
    Return 4.
    

![](https://assets.leetcode.com/uploads/2018/10/13/rainwater_empty.png)

The above image represents the elevation map `[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]` before the rain.



![](https://assets.leetcode.com/uploads/2018/10/13/rainwater_fill.png)

After the rain, water is trapped between the blocks. The total volume of water trapped is 4.


**Tags:** Heap, Breadth-first Search

**Difficulty:** Hard

**思路:**
