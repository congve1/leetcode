# 最佳买卖股票时机含冷冻期

## 描述

给定一个整数数组，其中第 _  i_ 个元素代表了第  _i_  天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

  * 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
  * 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

**示例:**

    
    
    **输入:** [1,2,3,0,2]
    **输出:** 3 
    **解释:** 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]



# Best Time to Buy and Sell Stock with Cooldown

## Description



Say you have an array for which the _i_ th element is the price of a given stock on day _i_.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

  * You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
  * After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

**Example:**

    
    
    **Input:** [1,2,3,0,2]
    **Output:** 3 
    **Explanation:** transactions = [buy, sell, cooldown, buy, sell]
    


**Tags:** Dynamic Programming

**Difficulty:** Medium

**思路:**
