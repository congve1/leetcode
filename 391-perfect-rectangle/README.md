# 完美矩形

## 描述

我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。

每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rectangle_perfect.gif)

**示例 1:**

    
    
    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [3,2,4,4],
      [1,3,2,4],
      [2,3,3,4]
    ]
    
    返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
    



![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rectangle_separated.gif)

**示例  2:**

    
    
    rectangles = [
      [1,1,2,3],
      [1,3,2,4],
      [3,1,4,2],
      [3,2,4,4]
    ]
    
    返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
    



![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rectangle_hole.gif)

**示例 3:**

    
    
    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [1,3,2,4],
      [3,2,4,4]
    ]
    
    返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
    



![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rectangle_intersect.gif)

**示例 4:**

    
    
    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [1,3,2,4],
      [2,2,4,4]
    ]
    
    返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
    



# Perfect Rectangle

## Description



Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

![](https://assets.leetcode.com/uploads/2018/10/22/rectangle_perfect.gif)

**Example 1:**

    
    
    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [3,2,4,4],
      [1,3,2,4],
      [2,3,3,4]
    ]
    
    Return true. All 5 rectangles together form an exact cover of a rectangular region.
    





![](https://assets.leetcode.com/uploads/2018/10/22/rectangle_separated.gif)

**Example 2:**

    
    
    rectangles = [
      [1,1,2,3],
      [1,3,2,4],
      [3,1,4,2],
      [3,2,4,4]
    ]
    
    Return false. Because there is a gap between the two rectangular regions.
    





![](https://assets.leetcode.com/uploads/2018/10/22/rectangle_hole.gif)

**Example 3:**

    
    
    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [1,3,2,4],
      [3,2,4,4]
    ]
    
    Return false. Because there is a gap in the top center.
    





![](https://assets.leetcode.com/uploads/2018/10/22/rectangle_intersect.gif)

**Example 4:**

    
    
    rectangles = [
      [1,1,3,3],
      [3,1,4,2],
      [1,3,2,4],
      [2,2,4,4]
    ]
    
    Return false. Because two of the rectangles overlap with each other.
    




**Tags:** 

**Difficulty:** Hard

**思路:**
