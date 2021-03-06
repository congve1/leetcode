# 最小区间

## 描述

你有 `k` 个升序排列的整数数组。找到一个 **最小** 区间，使得 `k` 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 `b-a < d-c` 或者在 `b-a == d-c` 时 `a < c`，则区间 [a,b] 比 [c,d] 小。

**示例 1:**

    
    
    **输入:** [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    **输出:** [20,24]
    **解释:** 
    列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
    列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
    列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
    

**注意:**

  1. 给定的列表可能包含重复元素，所以在这里升序表示 >= 。
  2. 1 <= `k` <= 3500
  3. -105 <= `元素的值` <= 105
  4. **对于使用Java的用户，请注意传入类型已修改为List <List<Integer>>。重置代码模板后可以看到这项改动。**



# Smallest Range

## Description



You have `k` lists of sorted integers in ascending order. Find the **smallest** range that includes at least one number from each of the `k` lists.

We define the range [a,b] is smaller than range [c,d] if `b-a < d-c` or `a < c` if `b-a == d-c`.

**Example 1:**  

    
    
    **Input:** [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    **Output:** [20,24]
    **Explanation:** 
    List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
    List 2: [0, 9, 12, 20], 20 is in range [20,24].
    List 3: [5, 18, 22, 30], 22 is in range [20,24].
    

**Note:**  

  1. The given list may contain duplicates, so ascending order means >= here.
  2. 1 <= `k` <= 3500
  3. -105 <= `value of elements` <= 105.
  4. **For Java users, please note that the input type has been changed to List <List<Integer>>. And after you reset the code template, you'll see this point.**

  


**Tags:** Hash Table, Two Pointers, String

**Difficulty:** Hard

**思路:**
