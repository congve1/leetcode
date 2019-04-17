# H指数

## 描述

给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 _h  _指数。

[h 指数的定义](https://baike.baidu.com/item/h-index/3991452?fr=aladdin): "h 代表"高引用次数"（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中） **至多** 有 h 篇论文分别被引用了 **至少** h 次。（其余的  _N - h  _篇论文每篇被引用次数 **不多于** _h_ 次。）"



**示例:**

    
    
    **输入:** citations = [3,0,6,1,5]
    **输出:** 3 
    **解释:** 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
         由于研究者有 3 篇论文每篇 **至少** 被引用了 3 次，其余两篇论文每篇被引用 **不多于** 3 次，所以她的 _h_ 指数是 3。



**说明:  **如果 _h_ 有多种可能的值， _h_ 指数是其中最大的那个。



# H-Index

## Description



Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): "A scientist has index _h_ if _h_ of his/her _N_ papers have **at least** _h_ citations each, and the other _N − h_ papers have **no more than** _h_ citations each."

**Example:**

    
    
    **Input:** citations = [3,0,6,1,5]
    **Output:** 3 
    **Explanation:**[3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
                 received 3, 0, 6, 1, 5 citations respectively. 
                 Since the researcher has 3 papers with **at least** 3 citations each and the remaining 
                 two with **no more than** 3 citations each, her h-index is 3.

**Note:  **If there are several possible values for _h_ , the maximum one is taken as the h-index.


**Tags:** Sort, Hash Table

**Difficulty:** Medium

**思路:**
