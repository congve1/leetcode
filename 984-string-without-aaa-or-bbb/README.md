# 不含 AAA 或 BBB 的字符串

## 描述

给定两个整数 `A` 和 `B`，返回 **任意** 字符串 `S`，要求满足：

  * `S` 的长度为 `A + B`，且正好包含 `A` 个 `'a'` 字母与 `B` 个 `'b'` 字母；
  * 子串 `'aaa'` 没有出现在 `S` 中；
  * 子串 `'bbb'` 没有出现在 `S` 中。



**示例 1：**

    
    
    **输入：** A = 1, B = 2
    **输出：** "abb"
    **解释：** "abb", "bab" 和 "bba" 都是正确答案。
    

**示例 2：**

    
    
    **输入：** A = 4, B = 1
    **输出：** "aabaa"



**提示：**

  1. `0 <= A <= 100`
  2. `0 <= B <= 100`
  3. 对于给定的 `A` 和 `B`，保证存在满足要求的 `S`。



# String Without AAA or BBB

## Description



Given two integers `A` and `B`, return **any** string `S` such that:

  * `S` has length `A + B` and contains exactly `A` `'a'` letters, and exactly `B` `'b'` letters;
  * The substring `'aaa'` does not occur in `S`;
  * The substring `'bbb'` does not occur in `S`.



**Example 1:**

    
    
    **Input:** A = 1, B = 2
    **Output:** "abb"
    **Explanation:** "abb", "bab" and "bba" are all correct answers.
    

**Example 2:**

    
    
    **Input:** A = 4, B = 1
    **Output:** "aabaa"



**Note:**

  1. `0 <= A <= 100`
  2. `0 <= B <= 100`
  3. It is guaranteed such an `S` exists for the given `A` and `B`.


**Tags:** Greedy

**Difficulty:** Medium

**思路:**
