# 通过删除字母匹配到字典里最长单词

## 描述

给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

**示例 1:**

    
    
    **输入:**
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
    
    **输出:** 
    "apple"
    

**示例  2:**

    
    
    **输入:**
    s = "abpcplea", d = ["a","b","c"]
    
    **输出:** 
    "a"
    

**说明:**

  1. 所有输入的字符串只包含小写字母。
  2. 字典的大小不会超过 1000。
  3. 所有输入的字符串长度不会超过 1000。



# Longest Word in Dictionary through Deleting

## Description



Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

**Example 1:**  

    
    
    **Input:**
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
    
    **Output:** 
    "apple"
    

**Example 2:**  

    
    
    **Input:**
    s = "abpcplea", d = ["a","b","c"]
    
    **Output:** 
    "a"
    

**Note:**  

  1. All the strings in the input will only contain lower-case letters.
  2. The size of the dictionary won't exceed 1,000.
  3. The length of all the strings in the input won't exceed 1,000.


**Tags:** Sort, Two Pointers

**Difficulty:** Medium

**思路:**
