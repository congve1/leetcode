# 字符串解码

## 描述

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: `k[encoded_string]`，表示其中方括号内部的 _encoded_string_ 正好重复 _k_ 次。注意 _k_ 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 _k_ ，例如不会出现像 `3a` 或 `2[4]` 的输入。

**示例:**

    
    
    s = "3[a]2[bc]", 返回 "aaabcbc".
    s = "3[a2[c]]", 返回 "accaccacc".
    s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
    



# Decode String

## Description



Given an encoded string, return it's decoded string.

The encoding rule is: `k[encoded_string]`, where the _encoded_string_ inside the square brackets is being repeated exactly _k_ times. Note that _k_ is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, _k_. For example, there won't be input like `3a` or `2[4]`.

**Examples:**

    
    
    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
    


**Tags:** Stack, Depth-first Search

**Difficulty:** Medium

**思路:**
