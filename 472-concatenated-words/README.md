# 连接词

## 描述

给定一个 **不含重复** 单词的列表，编写一个程序，返回给定单词列表中所有的连接词。

连接词的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。

**示例:**

    
    
    **输入:** ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    
    **输出:** ["catsdogcats","dogcatsdog","ratcatdogcat"]
    
    **解释:** "catsdogcats"由"cats", "dog" 和 "cats"组成; 
         "dogcatsdog"由"dog", "cats"和"dog"组成; 
         "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
    

**说明:**

  1. 给定数组的元素总数不超过 `10000`。
  2. 给定数组中元素的长度总和不超过 `600000`。
  3. 所有输入字符串只包含小写字母。
  4. 不需要考虑答案输出的顺序。



# Concatenated Words

## Description

Given a list of words ( **without duplicates** ), please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

**Example:**  

    
    
    **Input:** ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    
    **Output:** ["catsdogcats","dogcatsdog","ratcatdogcat"]
    
    **Explanation:** "catsdogcats" can be concatenated by "cats", "dog" and "cats";   
     "dogcatsdog" can be concatenated by "dog", "cats" and "dog";   
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
    

**Note:**  

  1. The number of elements of the given array will not exceed `10,000 `
  2. The length sum of elements in the given array will not exceed `600,000`. 
  3. All the input string will only include lower case letters.
  4. The returned elements order does not matter. 


**Tags:** Depth-first Search, Trie, Dynamic Programming

**Difficulty:** Hard

**思路:**
