# 最大平均值和的分组

## 描述

我们将给定的数组 `A` 分成 `K` 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。

注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。

    
    
    **示例:**
    **输入:** 
    A = [9,1,2,3,9]
    K = 3
    **输出:** 20
    **解释:** 
    A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
    我们也可以把 A 分成[9, 1], [2], [3, 9].
    这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
    

**说明:**

  * `1 <= A.length <= 100`.
  * `1 <= A[i] <= 10000`.
  * `1 <= K <= A.length`.
  * 答案误差在 `10^-6` 内被视为是正确的。



# Largest Sum of Averages

## Description



We partition a row of numbers `A` into at most `K` adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

    
    
    **Example:**
    **Input:** 
    A = [9,1,2,3,9]
    K = 3
    **Output:** 20
    **Explanation:** 
    The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
    We could have also partitioned A into [9, 1], [2], [3, 9], for example.
    That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
    



**Note:**

  * `1 <= A.length <= 100`.
  * `1 <= A[i] <= 10000`.
  * `1 <= K <= A.length`.
  * Answers within `10^-6` of the correct answer will be accepted as correct.


**Tags:** Dynamic Programming

**Difficulty:** Medium

**思路:**
