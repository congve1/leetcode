# 最大为 N 的数字组合

## 描述

我们有一组 **排序的** 数字 `D`，它是  `{'1','2','3','4','5','6','7','8','9'}` 的非空子集。（请注意，`'0'` 不包括在内。）

现在，我们用这些数字进行组合写数字，想用多少次就用多少次。例如 `D = {'1','3','5'}`，我们可以写出像 `'13', '551', '1351315'` 这样的数字。

返回可以用 `D` 中的数字写出的小于或等于 `N` 的正整数的数目。



**示例 1：**

    
    
    **输入：** D = ["1","3","5","7"], N = 100
    **输出：** 20
    **解释：**
    可写出的 20 个数字是：
    1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
    

**示例 2：**

    
    
    **输入：** D = ["1","4","9"], N = 1000000000
    **输出：** 29523
    **解释：**
    我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
    81 个四位数字，243 个五位数字，729 个六位数字，
    2187 个七位数字，6561 个八位数字和 19683 个九位数字。
    总共，可以使用D中的数字写出 29523 个整数。



**提示：**

  1. `D` 是按排序顺序的数字 `'1'-'9'` 的子集。
  2. `1 <= N <= 10^9`



# Numbers At Most N Given Digit Set

## Description



We have a **sorted** set of digits `D`, a non-empty subset of `{'1','2','3','4','5','6','7','8','9'}`.  (Note that `'0'` is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if `D = {'1','3','5'}`, we may write numbers such as `'13', '551', '1351315'`.

Return the number of positive integers that can be written (using the digits of `D`) that are less than or equal to `N`.



**Example 1:**

    
    
    **Input:** D = ["1","3","5","7"], N = 100
    **Output:** 20
    **Explanation:**
    The 20 numbers that can be written are:
    1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
    

**Example 2:**

    
    
    **Input:** D = ["1","4","9"], N = 1000000000
    **Output:** 29523
    **Explanation:**
    We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
    81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
    2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
    In total, this is 29523 integers that can be written using the digits of D.



**Note:**

  1. `D` is a subset of digits `'1'-'9'` in sorted order.
  2. `1 <= N <= 10^9`


**Tags:** Math, Dynamic Programming

**Difficulty:** Hard

**思路:**
