# 删列造序 III

## 描述

给定由 `N` 个小写字母字符串组成的数组 `A`，其中每个字符串长度相等。

选取一个删除索引序列，对于 `A` 中的每个字符串，删除对应每个索引处的字符。

比如，有 `A = ["babca","bbazb"]`，删除索引序列 `{0, 1, 4}`，删除后 `A` 为`["bc","az"]`。

假设，我们选择了一组删除索引 `D`，那么在执行删除操作之后，最终得到的数组的行中的每个元素都是按 **字典序** 排列的。

清楚起见，`A[0]` 是按字典序排列的（即，`A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]`），`A[1]` 是按字典序排列的（即，`A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]`），依此类推。

请你返回 `D.length` 的最小可能值。



**示例 1：**

    
    
    **输入：** ["babca","bbazb"]
    **输出：** 3
    **解释：** 删除 0、1 和 4 这三列后，最终得到的数组是 A = ["bc", "az"]。
    这两行是分别按字典序排列的（即，A[0][0] <= A[0][1] 且 A[1][0] <= A[1][1]）。
    注意，A[0] > A[1] ---- 数组 A 不一定是按字典序排列的。
    

**示例 2：**

    
    
    **输入：** ["edcba"]
    **输出：** 4
    **解释：** 如果删除的列少于 4 列，则剩下的行都不会按字典序排列。
    

**示例 3：**

    
    
    **输入：** ["ghi","def","abc"]
    **输出：** 0
    **解释：** 所有行都已按字典序排列。
    



**提示：**

  1. `1 <= A.length <= 100`
  2. `1 <= A[i].length <= 100`



# Delete Columns to Make Sorted III

## Description



We are given an array `A` of `N` lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array `A = ["babca","bbazb"]` and deletion indices `{0, 1, 4}`, then the final array after deletions is `["bc","az"]`.

Suppose we chose a set of deletion indices `D` such that after deletions, the final array has **every element (row) in  lexicographic** order.

For clarity, `A[0]` is in lexicographic order (ie. `A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]`), `A[1]` is in lexicographic order (ie. `A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]`), and so on.

Return the minimum possible value of `D.length`.



**Example 1:**

    
    
    **Input:** ["babca","bbazb"]
    **Output:** 3
    **Explanation:** After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
    Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
    Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.
    

**Example 2:**

    
    
    **Input:** ["edcba"]
    **Output:** 4
    **Explanation:** If we delete less than 4 columns, the only row won't be lexicographically sorted.
    

**Example 3:**

    
    
    **Input:** ["ghi","def","abc"]
    **Output:** 0
    **Explanation:** All rows are already lexicographically sorted.
    



**Note:**

  1. `1 <= A.length <= 100`
  2. `1 <= A[i].length <= 100`


**Tags:** Dynamic Programming

**Difficulty:** Hard

**思路:**
