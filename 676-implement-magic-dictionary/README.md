# 实现一个魔法字典

## 描述

实现一个带有`buildDict`, 以及 `search`方法的魔法字典。

对于`buildDict`方法，你将被给定一串不重复的单词来构建一个字典。

对于`search`方法，你将被给定一个单词，并且判定能否只将这个单词中 **一个** 字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

**示例 1:**

    
    
    Input: buildDict(["hello", "leetcode"]), Output: Null
    Input: search("hello"), Output: False
    Input: search("hhllo"), Output: True
    Input: search("hell"), Output: False
    Input: search("leetcoded"), Output: False
    

**注意:**

  1. 你可以假设所有输入都是小写字母 `a-z`。
  2. 为了便于竞赛，测试所用的数据量很小。你可以在竞赛结束后，考虑更高效的算法。
  3. 请记住 **重置** MagicDictionary类中声明的类变量，因为静态/类变量会在多个测试用例中保留。 请参阅[这里](http://leetcode.com/faq/#different-output)了解更多详情。



# Implement Magic Dictionary

## Description



Implement a magic directory with `buildDict`, and `search` methods.

For the method `buildDict`, you'll be given a list of non-repetitive words to build a dictionary.

For the method `search`, you'll be given a word, and judge whether if you modify **exactly** one character into **another** character in this word, the modified word is in the dictionary you just built.

**Example 1:**  

    
    
    Input: buildDict(["hello", "leetcode"]), Output: Null
    Input: search("hello"), Output: False
    Input: search("hhllo"), Output: True
    Input: search("hell"), Output: False
    Input: search("leetcoded"), Output: False
    

**Note:**  

  1. You may assume that all the inputs are consist of lowercase letters `a-z`.
  2. For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
  3. Please remember to **RESET** your class variables declared in class MagicDictionary, as static/class variables are **persisted across multiple test cases**. Please see [here](https://leetcode.com/faq/#different-output) for more details.


**Tags:** Trie, Hash Table

**Difficulty:** Medium

**思路:**
