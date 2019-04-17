# 总持续时间可被 60 整除的歌曲

## 描述

在歌曲列表中，第 `i` 首歌曲的持续时间为 `time[i]` 秒。

返回其总持续时间（以秒为单位）可被 `60` 整除的歌曲对的数量。形式上，我们希望索引的数字  `i < j` 且有 `(time[i] + time[j]) % 60 == 0`。



**示例 1：**

    
    
    **输入：** [30,20,150,100,40]
    **输出：** 3
    **解释：** 这三对的总持续时间可被 60 整数：
    (time[0] = 30, time[2] = 150): 总持续时间 180
    (time[1] = 20, time[3] = 100): 总持续时间 120
    (time[1] = 20, time[4] = 40): 总持续时间 60
    

**示例 2：**

    
    
    **输入：** [60,60,60]
    **输出：** 3
    **解释：** 所有三对的总持续时间都是 120，可以被 60 整数。
    



**提示：**

  1. `1 <= time.length <= 60000`
  2. `1 <= time[i] <= 500`



# Pairs of Songs With Total Durations Divisible by 60

## Description



In a list of songs, the `i`-th song has a duration of `time[i]` seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by `60`.  Formally, we want the number of indices `i < j` with `(time[i] + time[j]) % 60 == 0`.



**Example 1:**

    
    
    **Input:** [30,20,150,100,40]
    **Output:** 3
    **Explanation:** Three pairs have a total duration divisible by 60:
    (time[0] = 30, time[2] = 150): total duration 180
    (time[1] = 20, time[3] = 100): total duration 120
    (time[1] = 20, time[4] = 40): total duration 60
    

**Example 2:**

    
    
    **Input:** [60,60,60]
    **Output:** 3
    **Explanation:** All three pairs have a total duration of 120, which is divisible by 60.
    



**Note:**

  1. `1 <= time.length <= 60000`
  2. `1 <= time[i] <= 500`


**Tags:** Array

**Difficulty:** Easy

**思路:**
