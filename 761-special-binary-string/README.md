# 特殊的二进制序列

## 描述

特殊的二进制序列是具有以下两个性质的二进制序列：

  * 0 的数量与 1 的数量相等。
  * 二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。

给定一个特殊的二进制序列 `S`，以字符串形式表示。定义一个 _操作_ 为首先选择 `S` 的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)

在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？

**示例 1:**

    
    
    **输入:** S = "11011000"
    **输出:** "11100100"
    **解释:**
    将子串 "10" （在S[1]出现） 和 "1100" （在S[3]出现）进行交换。
    这是在进行若干次操作后按字典序排列最大的结果。
    

**说明:**

  1. `S` 的长度不超过 `50`。
  2. `S` 保证为一个满足上述定义的 _特殊_ 的二进制序列。



# Special Binary String

## Description



_Special_ binary strings are binary strings with the following two properties:

* The number of 0's is equal to the number of 1's.
* Every prefix of the binary string has at least as many 1's as 0's.

Given a special string `S`, a _move_ consists of choosing two consecutive, non-empty, special substrings of `S`, and swapping them. _(Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)_

At the end of any number of moves, what is the lexicographically largest resulting string possible?

**Example 1:**  

    
    
    **Input:** S = "11011000"
    **Output:** "11100100"
    **Explanation:**
    The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
    This is the lexicographically largest string possible after some number of swaps.
    

**Note:**

  1. `S` has length at most `50`.
  2. `S` is guaranteed to be a _special_ binary string as defined above.


**Tags:** Recursion, String

**Difficulty:** Hard

**思路:**
