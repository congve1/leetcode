# 单词搜索

## 描述

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中"相邻"单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例:**

    
    
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    
    给定 word = " **ABCCED** ", 返回 **true**.
    给定 word = " **SEE** ", 返回 **true**.
    给定 word = " **ABCB** ", 返回 **false**.



# Word Search

## Description



Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**

    
    
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    
    Given word = " **ABCCED** ", return **true**.
    Given word = " **SEE** ", return **true**.
    Given word = " **ABCB** ", return **false**.
    


**Tags:** Array, Backtracking

**Difficulty:** Medium

**思路:**