# 重复叠加字符串匹配

## 描述

给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。

举个例子，A = "abcd"，B = "cdabcdab"。

答案为 3， 因为 A 重复叠加三遍后为 "abcdabcdabcd"，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。

**注意:**

 `A` 与 `B` 字符串的长度在1和10000区间范围内。



# Repeated String Match

## Description



Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

**Note:**  
The length of `A` and `B` will be between 1 and 10000.


**Tags:** String

**Difficulty:** Easy

**思路:**
