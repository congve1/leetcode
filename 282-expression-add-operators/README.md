# 给表达式添加运算符

## 描述

给定一个仅包含数字 `0-9` 的字符串和一个目标值，在数字之间添加 **二元** 运算符（不是一元）`+`、`-` 或 `*` ，返回所有能够得到目标值的表达式。

**示例 1:**

    
    
    **输入:** _num_ = "123", _target_ = 6
    **输出:** ["1+2+3", "1*2*3"] 
    

**示例  2:**

    
    
    **输入:** _num_ = "232", _target_ = 8
    **输出:** ["2*3+2", "2+3*2"]

**示例 3:**

    
    
    **输入:** _num_ = "105", _target_ = 5
    **输出:** ["1*0+5","10-5"]

**示例  4:**

    
    
    **输入:** _num_ = "00", _target_ = 0
    **输出:** ["0+0", "0-0", "0*0"]
    

**示例 5:**

    
    
    **输入:** _num_ = "3456237490", _target_ = 9191
    **输出:** []
    



# Expression Add Operators

## Description



Given a string that contains only digits `0-9` and a target value, return all possibilities to add **binary** operators (not unary) `+`, `-`, or `*` between the digits so they evaluate to the target value.

**Example 1:**

    
    
    **Input:** _num_ = "123", _target_ = 6
    **Output:** ["1+2+3", "1*2*3"] 
    

**Example 2:**

    
    
    **Input:** _num_ = "232", _target_ = 8
    **Output:** ["2*3+2", "2+3*2"]

**Example 3:**

    
    
    **Input:** _num_ = "105", _target_ = 5
    **Output:** ["1*0+5","10-5"]

**Example 4:**

    
    
    **Input:** _num_ = "00", _target_ = 0
    **Output:** ["0+0", "0-0", "0*0"]
    

**Example 5:**

    
    
    **Input:** _num_ = "3456237490", _target_ = 9191
    **Output:** []
    


**Tags:** Divide and Conquer

**Difficulty:** Hard

**思路:**
