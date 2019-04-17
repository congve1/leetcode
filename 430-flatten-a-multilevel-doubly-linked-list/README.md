# 扁平化多级双向链表

## 描述

您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。



**示例:**

    
    
    **输入:**
     1---2---3---4---5---6--NULL
             |
             7---8---9---10--NULL
                 |
                 11--12--NULL
    
    **输出:**
    1-2-3-7-8-11-12-9-10-4-5-6-NULL
    



**以上示例的说明:**

给出以下多级双向链表:

    
    
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/multilevellinkedlist.png)



我们应该返回如下所示的扁平双向链表:

    
    
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/multilevellinkedlistflattened.png)



# Flatten a Multilevel Doubly Linked List

## Description



You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



**Example:**

    
    
    **Input:**
     1---2---3---4---5---6--NULL
             |
             7---8---9---10--NULL
                 |
                 11--12--NULL
    
    **Output:**
    1-2-3-7-8-11-12-9-10-4-5-6-NULL
    



**Explanation for the above example:**

Given the following multilevel doubly linked list:

    
    
    ![](https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlist.png)



We should return the following flattened doubly linked list:

    
    
    ![](https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlistflattened.png)


**Tags:** Depth-first Search, Linked List

**Difficulty:** Medium

**思路:**
