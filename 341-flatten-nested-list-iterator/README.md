# 扁平化嵌套列表迭代器

## 描述

给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的项或者为一个整数，或者是另一个列表。

**示例 1:**

    
    
    **输入:** [[1,1],2,[1,1]]
    **输出:** [1,1,2,1,1]
    **解释:** 通过重复调用  _next_ 直到  _hasNex_ t 返回false， _next  _返回的元素的顺序应该是: [1,1,2,1,1]。

**示例 2:**

    
    
    **输入:** [1,[4,[6]]]
    **输出:** [1,4,6]
    **解释:** 通过重复调用  _next  _直到  _hasNex_ t 返回false， _next  _返回的元素的顺序应该是: [1,4,6]。
    



# Flatten Nested List Iterator

## Description



Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

**Example 1:**

    
    
    **Input:** [[1,1],2,[1,1]]
    **Output:** [1,1,2,1,1]
    **Explanation:** By calling _next_ repeatedly until _hasNext_ returns false, 
                 the order of elements returned by _next_ should be: [1,1,2,1,1].

**Example 2:**

    
    
    **Input:** [1,[4,[6]]]
    **Output:** [1,4,6]
    **Explanation:** By calling _next_ repeatedly until _hasNext_ returns false, 
                 the order of elements returned by _next_ should be: [1,4,6].
    


**Tags:** Stack, Design

**Difficulty:** Medium

**思路:**
