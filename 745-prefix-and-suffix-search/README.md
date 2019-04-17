# 前缀和后缀搜索

## 描述

给定多个 `words`，`words[i]` 的权重为 `i` 。

设计一个类 `WordFilter` 实现函数`WordFilter.f(String prefix, String suffix)`。这个函数将返回具有前缀 `prefix` 和后缀`suffix` 的词的最大权重。如果没有这样的词，返回 -1。

**例子:**

    
    
    **输入:**
    WordFilter(["apple"])
    WordFilter.f("a", "e") // 返回 0
    WordFilter.f("b", "") // 返回 -1
    

**注意:**

  1. `words`的长度在`[1, 15000]`之间。
  2. 对于每个测试用例，最多会有`words.length`次对`WordFilter.f`的调用。
  3. `words[i]`的长度在`[1, 10]`之间。
  4. `prefix, suffix`的长度在`[0, 10]`之前。
  5. `words[i]`和`prefix, suffix`只包含小写字母。



# Prefix and Suffix Search

## Description



Given many `words`, `words[i]` has weight `i`.

Design a class `WordFilter` that supports one function, `WordFilter.f(String prefix, String suffix)`. It will return the word with given `prefix` and `suffix` with maximum weight. If no word exists, return -1.

**Examples:**

    
    
    **Input:**
    WordFilter(["apple"])
    WordFilter.f("a", "e") // returns 0
    WordFilter.f("b", "") // returns -1
    



**Note:**

  1. `words` has length in range `[1, 15000]`.
  2. For each test case, up to `words.length` queries `WordFilter.f` may be made.
  3. `words[i]` has length in range `[1, 10]`.
  4. `prefix, suffix` have lengths in range `[0, 10]`.
  5. `words[i]` and `prefix, suffix` queries consist of lowercase letters only.




**Tags:** Trie

**Difficulty:** Hard

**思路:**
