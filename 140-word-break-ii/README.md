# 单词拆分 II

## 描述

给定一个 **非空** 字符串 _s_ 和一个包含 **非空** 单词列表的字典 _wordDict_ ，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

**说明：**

  * 分隔时可以重复使用字典中的单词。
  * 你可以假设字典中没有重复的单词。

**示例 1：**

    
    
    **输入:** s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    **输出:**[
      "cats and dog",
      "cat sand dog"
    ]
    

**示例 2：**

    
    
    **输入:** s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    **输出:** [
      "pine apple pen apple",
      "pineapple pen apple",
      "pine applepen apple"
    ]
    **解释:** 注意你可以重复使用字典中的单词。
    

**示例  3：**

    
    
    **输入:** s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    **输出:** []
    



# Word Break II

## Description



Given a **non-empty** string _s_ and a dictionary _wordDict_ containing a list of **non-empty** words, add spaces in _s_ to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

**Note:**

  * The same word in the dictionary may be reused multiple times in the segmentation.
  * You may assume the dictionary does not contain duplicate words.

**Example 1:**

    
    
    **Input:** s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    **Output:**[
      "cats and dog",
      "cat sand dog"
    ]
    

**Example 2:**

    
    
    **Input:** s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    **Output:** [
      "pine apple pen apple",
      "pineapple pen apple",
      "pine applepen apple"
    ]
    **Explanation:** Note that you are allowed to reuse a dictionary word.
    

**Example 3:**

    
    
    **Input:** s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    **Output:** []


**Tags:** Dynamic Programming, Backtracking

**Difficulty:** Hard

**思路:**
