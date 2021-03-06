# 单词拆分

## 描述

给定一个 **非空** 字符串 _s_ 和一个包含 **非空** 单词列表的字典 _wordDict_ ，判定  _s_ 是否可以被空格拆分为一个或多个在字典中出现的单词。

**说明：**

  * 拆分时可以重复使用字典中的单词。
  * 你可以假设字典中没有重复的单词。

**示例 1：**

    
    
    **输入:** s = "leetcode", wordDict = ["leet", "code"]
    **输出:** true
    **解释:** 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
    

**示例 2：**

    
    
    **输入:** s = "applepenapple", wordDict = ["apple", "pen"]
    **输出:** true
    **解释:** 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
         注意你可以重复使用字典中的单词。
    

**示例 3：**

    
    
    **输入:** s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    **输出:** false
    



# Word Break

## Description



Given a **non-empty** string _s_ and a dictionary _wordDict_ containing a list of **non-empty** words, determine if _s_ can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

  * The same word in the dictionary may be reused multiple times in the segmentation.
  * You may assume the dictionary does not contain duplicate words.

**Example 1:**

    
    
    **Input:** s = "leetcode", wordDict = ["leet", "code"]
    **Output:** true
    **Explanation:** Return true because "leetcode" can be segmented as "leet code".
    

**Example 2:**

    
    
    **Input:** s = "applepenapple", wordDict = ["apple", "pen"]
    **Output:** true
    **Explanation:** Return true because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.
    

**Example 3:**

    
    
    **Input:** s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    **Output:** false
    


**Tags:** Dynamic Programming

**Difficulty:** Medium

**思路:**
