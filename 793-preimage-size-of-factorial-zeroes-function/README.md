# 阶乘函数后K个零

## 描述

 `f(x)` 是 `x!` 末尾是0的数量。（回想一下 `x! = 1 * 2 * 3 * ... * x`，且`0! = 1`）

例如， `f(3) = 0` ，因为3! = 6的末尾没有0；而 `f(11) = 2` ，因为11!= 39916800末端有2个0。给定 `K`，找出多少个非负整数`x` ，有 `f(x) = K` 的性质。

    
    
    **示例 1:
    输入:** K = 0 **输出:** 5 **解释:**  0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。 **示例 2:
    输入:** K = 5 **输出:** 0 **解释:** 没有匹配到这样的 x!，符合K = 5 的条件 **。**
    

**注意：**

  * `K`是范围在 `[0, 10^9]` 的整数 **。**



# Preimage Size of Factorial Zeroes Function

## Description



Let `f(x)` be the number of zeroes at the end of `x!`. (Recall that `x! = 1 * 2 * 3 * ... * x`, and by convention, `0! = 1`.)

For example, `f(3) = 0` because 3! = 6 has no zeroes at the end, while `f(11) = 2` because 11! = 39916800 has 2 zeroes at the end. Given `K`, find how many non-negative integers `x` have the property that `f(x) = K`.

    
    
    **Example 1:**
    **Input:** K = 0
    **Output:** 5
    **Explanation:** 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.
    
    **Example 2:**
    **Input:** K = 5
    **Output:** 0
    **Explanation:** There is no x such that x! ends in K = 5 zeroes.
    

**Note:**

  * `K` will be an integer in the range `[0, 10^9]`.


**Tags:** Binary Search

**Difficulty:** Hard

**思路:**
