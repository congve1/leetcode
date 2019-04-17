# 单词接龙

## 描述

给定两个单词（ _beginWord  _和 _endWord_ ）和一个字典，找到从  _beginWord_ 到  _endWord_ 的最短转换序列的长度。转换需遵循如下规则：

  1. 每次转换只能改变一个字母。
  2. 转换过程中的中间单词必须是字典中的单词。

**说明:**

  * 如果不存在这样的转换序列，返回 0。
  * 所有单词具有相同的长度。
  * 所有单词只由小写字母组成。
  * 字典中不存在重复的单词。
  * 你可以假设 _beginWord_ 和 _endWord_ 是非空的，且二者不相同。

**示例  1:**

    
    
    **输入:**
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    **输出:** 5
    
    **解释:** 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
         返回它的长度 5。
    

**示例 2:**

    
    
    **输入:**
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    **输出:**  0
    
    **解释:**   _endWord_ "cog" 不在字典中，所以无法进行转换。



# Word Ladder

## Description



Given two words ( _beginWord_ and _endWord_ ), and a dictionary's word list, find the length of shortest transformation sequence from _beginWord_ to _endWord_ , such that:

  1. Only one letter can be changed at a time.
  2. Each transformed word must exist in the word list. Note that _beginWord_ is _not_ a transformed word.

**Note:**

  * Return 0 if there is no such transformation sequence.
  * All words have the same length.
  * All words contain only lowercase alphabetic characters.
  * You may assume no duplicates in the word list.
  * You may assume _beginWord_ and _endWord_ are non-empty and are not the same.

**Example 1:**

    
    
    **Input:**
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    
    **Output:** 5
    
    **Explanation:** As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
    

**Example 2:**

    
    
    **Input:**
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    **Output:**  0
    
    **Explanation:**  The endWord "cog" is not in wordList, therefore no possible ** ** transformation.
    


**Tags:** Breadth-first Search

**Difficulty:** Medium

**思路:**
