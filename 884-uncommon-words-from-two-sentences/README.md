# 两句话中的不常见单词

## 描述

给定两个句子 `A` 和 `B` 。 （ _句子_ 是一串由空格分隔的单词。每个 _单词_ 仅由小写字母组成。）

如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是 _不常见的_ 。

返回所有不常用单词的列表。

您可以按任何顺序返回列表。



**示例 1：**

    
    
    **输入：** A = "this apple is sweet", B = "this apple is sour"
    **输出：** ["sweet","sour"]
    

**示例  2：**

    
    
    **输入：** A = "apple apple", B = "banana"
    **输出：** ["banana"]
    



**提示：**

  1. `0 <= A.length <= 200`
  2. `0 <= B.length <= 200`
  3. `A` 和 `B` 都只包含空格和小写字母。



# Uncommon Words from Two Sentences

## Description



We are given two sentences `A` and `B`.  (A _sentence_  is a string of space separated words.  Each _word_ consists only of lowercase letters.)

A word is _uncommon_  if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



**Example 1:**

    
    
    **Input:** A = "this apple is sweet", B = "this apple is sour"
    **Output:** ["sweet","sour"]
    

**Example 2:**

    
    
    **Input:** A = "apple apple", B = "banana"
    **Output:** ["banana"]
    



**Note:**

  1. `0 <= A.length <= 200`
  2. `0 <= B.length <= 200`
  3. `A` and `B` both contain only spaces and lowercase letters.


**Tags:** Hash Table

**Difficulty:** Easy

**思路:**
