# 用 Rand7() 实现 Rand10()

## 描述

已有方法 `rand7` 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 `rand10` 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 `Math.random()` 方法。



**示例 1:**

    
    
    **输入:** 1
    **输出:** [7]
    

**示例 2:**

    
    
    **输入:** 2
    **输出:** [8,4]
    

**示例 3:**

    
    
    **输入:** 3
    **输出:** [8,1,10]
    



**提示:**

  1. `rand7` 已定义。
  2. 传入参数: `n` 表示 `rand10` 的调用次数。



**进阶:**

  1. `rand7()`调用次数的 [期望值](https://en.wikipedia.org/wiki/Expected_value) 是多少 ?
  2. 你能否尽量少调用 `rand7()` ?



# Implement Rand10() Using Rand7()

## Description



Given a function `rand7` which generates a uniform random integer in the range 1 to 7, write a function `rand10` which generates a uniform random integer in the range 1 to 10.

Do NOT use system's `Math.random()`.



**Example 1:**

    
    
    **Input:** 1
    **Output:** [7]
    

**Example 2:**

    
    
    **Input:** 2
    **Output:** [8,4]
    

**Example 3:**

    
    
    **Input:** 3
    **Output:** [8,1,10]
    



**Note:**

  1. `rand7` is predefined.
  2. Each testcase has one argument: `n`, the number of times that `rand10` is called.



**Follow up:**

  1. What is the [expected value](https://en.wikipedia.org/wiki/Expected_value) for the number of calls to `rand7()` function?
  2. Could you minimize the number of calls to `rand7()`?


**Tags:** Random, Rejection Sampling

**Difficulty:** Medium

**思路:**
