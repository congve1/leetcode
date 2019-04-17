# 煎饼排序

## 描述

给定数组 `A`，我们可以对其进行 _煎饼翻转_ ：我们选择一些正整数 ` **k**  <= A.length`，然后反转 `A` 的前 **k**  个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 `A` 的排序。

返回能使 `A` 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 `10 * A.length` 范围内的有效答案都将被判断为正确。



**示例 1：**

    
    
    **输入：** [3,2,4,1]
    **输出：** [4,2,4,3]
    **解释：**
    我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
    初始状态 A = [3, 2, 4, 1]
    第一次翻转后 (k=4): A = [1, 4, 2, 3]
    第二次翻转后 (k=2): A = [4, 1, 2, 3]
    第三次翻转后 (k=4): A = [3, 2, 1, 4]
    第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。 
    

**示例 2：**

    
    
    **输入：** [1,2,3]
    **输出：** []
    **解释：** 输入已经排序，因此不需要翻转任何内容。
    请注意，其他可能的答案，如[3，3]，也将被接受。
    



**提示：**

  1. `1 <= A.length <= 100`
  2. `A[i]` 是 `[1, 2, ..., A.length]` 的排列



# Pancake Sorting

## Description



Given an array `A`, we can perform a  _pancake flip_ : We choose some positive integer ` **k** <= A.length`, then reverse the order of the first **k** elements of `A`.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array `A`.

Return the k-values corresponding to a sequence of pancake flips that sort `A`.  Any valid answer that sorts the array within `10 * A.length` flips will be judged as correct.



**Example 1:**

    
    
    **Input:** [3,2,4,1]
    **Output:** [4,2,4,3]
    **Explanation:**
    We perform 4 pancake flips, with k values 4, 2, 4, and 3.
    Starting state: A = [3, 2, 4, 1]
    After 1st flip (k=4): A = [1, 4, 2, 3]
    After 2nd flip (k=2): A = [4, 1, 2, 3]
    After 3rd flip (k=4): A = [3, 2, 1, 4]
    After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
    

**Example 2:**

    
    
    **Input:** [1,2,3]
    **Output:** []
    **Explanation:** The input is already sorted, so there is no need to flip anything.
    Note that other answers, such as [3, 3], would also be accepted.
    



**Note:**

  1. `1 <= A.length <= 100`
  2. `A[i]` is a permutation of `[1, 2, ..., A.length]`


**Tags:** Sort, Array

**Difficulty:** Medium

**思路:**
