# 公平的糖果交换

## 描述

爱丽丝和鲍勃有不同大小的糖果棒：`A[i]` 是爱丽丝拥有的第 `i` 块糖的大小，`B[j]` 是鲍勃拥有的第 `j` 块糖的大小。

因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。 _（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）_

返回一个整数数组 `ans`，其中 `ans[0]` 是爱丽丝必须交换的糖果棒的大小，`ans[1]` 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个。保证答案存在。



**示例 1：**

    
    
    **输入：** A = [1,1], B = [2,2]
    **输出：** [1,2]
    

**示例 2：**

    
    
    **输入：** A = [1,2], B = [2,3]
    **输出：** [1,2]
    

**示例 3：**

    
    
    **输入：** A = [2], B = [1,3]
    **输出：** [2,3]
    

**示例 4：**

    
    
    **输入：** A = [1,2,5], B = [2,4]
    **输出：** [5,4]
    



**提示：**

  * `1 <= A.length <= 10000`
  * `1 <= B.length <= 10000`
  * `1 <= A[i] <= 100000`
  * `1 <= B[i] <= 100000`
  * 保证爱丽丝与鲍勃的糖果总量不同。
  * 答案肯定存在。



# Fair Candy Swap

## Description



Alice and Bob have candy bars of different sizes: `A[i]` is the size of the `i`-th bar of candy that Alice has, and `B[j]` is the size of the `j`-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  ( _The total amount of candy  a person has is the sum of the sizes of candy bars they have._)

Return an integer array `ans` where `ans[0]` is the size of the candy bar that Alice must exchange, and `ans[1]` is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.



**Example 1:**

    
    
    **Input:** A = [1,1], B = [2,2]
    **Output:** [1,2]
    

**Example 2:**

    
    
    **Input:** A = [1,2], B = [2,3]
    **Output:** [1,2]
    

**Example 3:**

    
    
    **Input:** A = [2], B = [1,3]
    **Output:** [2,3]
    

**Example 4:**

    
    
    **Input:** A = [1,2,5], B = [2,4]
    **Output:** [5,4]
    



**Note:**

  * `1 <= A.length <= 10000`
  * `1 <= B.length <= 10000`
  * `1 <= A[i] <= 100000`
  * `1 <= B[i] <= 100000`
  * It is guaranteed that Alice and Bob have different total amounts of candy.
  * It is guaranteed there exists an answer.


**Tags:** Array

**Difficulty:** Easy

**思路:**
