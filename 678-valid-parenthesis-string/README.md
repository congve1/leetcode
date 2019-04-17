# 有效的括号字符串

## 描述

给定一个只包含三种字符的字符串：`（ `，`）` 和 `*`，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

  1. 任何左括号 `(` 必须有相应的右括号 `)`。
  2. 任何右括号 `)` 必须有相应的左括号 `(` 。
  3. 左括号 `(` 必须在对应的右括号之前 `)`。
  4. `*` 可以被视为单个右括号 `)` ，或单个左括号 `(` ，或一个空字符串。
  5. 一个空字符串也被视为有效字符串。

**示例 1:**

    
    
    **输入:** "()"
    **输出:** True
    

**示例 2:**

    
    
    **输入:** "(*)"
    **输出:** True
    

**示例 3:**

    
    
    **输入:** "(*))"
    **输出:** True
    

**注意:**

  1. 字符串大小将在 [1，100] 范围内。



# Valid Parenthesis String

## Description



Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

  1. Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
  2. Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
  3. Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
  4. `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string.
  5. An empty string is also valid.

**Example 1:**  

    
    
    **Input:** "()"
    **Output:** True
    

**Example 2:**  

    
    
    **Input:** "(*)"
    **Output:** True
    

**Example 3:**  

    
    
    **Input:** "(*))"
    **Output:** True
    

**Note:**  

  1. The string size will be in the range [1, 100].


**Tags:** String

**Difficulty:** Medium

**思路:**
