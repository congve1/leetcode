# 猜数字大小

## 描述

我们正在玩一个猜数字游戏。 游戏规则如下：  
我从  **1**  到  _ **n**_  选择一个数字。 你需要猜我选择了哪个数字。  
每次你猜错了，我会告诉你这个数字是大了还是小了。  
你调用一个预先定义好的接口 `guess(int num)`，它会返回 3 个可能的结果（`-1`，`1` 或 `0`）：

    
    
    -1 : 我的数字比较小
     1 : 我的数字比较大
     0 : 恭喜！你猜对了！
    

**示例 :**

    
    
    **输入:** n = 10, pick = 6
    **输出:** 6



# Guess Number Higher or Lower

## Description



We are playing the Guess Game. The game is as follows:

I pick a number from **1** to **_n_**. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API `guess(int num)` which returns 3 possible results (`-1`, `1`, or `0`):

    
    
    -1 : My number is lower
     1 : My number is higher
     0 : Congrats! You got it!
    

**Example :**

    
    
    **Input:** n = 10, pick = 6
    **Output:** 6
    


**Tags:** Binary Search

**Difficulty:** Easy

**思路:**
