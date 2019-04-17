# 编辑距离

## 描述

给定两个单词  _word1_ 和  _word2_ ，计算出将  _word1_  转换成  _word2_ 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

  1. 插入一个字符
  2. 删除一个字符
  3. 替换一个字符

**示例  1:**

    
    
    **输入:** word1 = "horse", word2 = "ros"
    **输出:** 3
    **解释:** 
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')
    

**示例  2:**

    
    
    **输入:** word1 = "intention", word2 = "execution"
    **输出:** 5
    **解释:** 
    intention -> inention (删除 't')
    inention -> enention (将 'i' 替换为 'e')
    enention -> exention (将 'n' 替换为 'x')
    exention -> exection (将 'n' 替换为 'c')
    exection -> execution (插入 'u')
    



# Edit Distance

## Description



Given two words _word1_ and _word2_ , find the minimum number of operations required to convert _word1_ to _word2_.

You have the following 3 operations permitted on a word:

  1. Insert a character
  2. Delete a character
  3. Replace a character

**Example 1:**

    
    
    **Input:** word1 = "horse", word2 = "ros"
    **Output:** 3
    **Explanation:** 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
    

**Example 2:**

    
    
    **Input:** word1 = "intention", word2 = "execution"
    **Output:** 5
    **Explanation:** 
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
    


**Tags:** String, Dynamic Programming

**Difficulty:** Hard

**思路:**
