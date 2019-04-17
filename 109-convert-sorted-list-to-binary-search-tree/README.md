# 有序链表转换二叉搜索树

## 描述

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树 _每个节点  _的左右两个子树的高度差的绝对值不超过 1。

**示例:**

    
    
    给定的有序链表： [-10, -3, 0, 5, 9],
    
    一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
    
          0
         / \
       -3   9
       /   /
     -10  5
    



# Convert Sorted List to Binary Search Tree

## Description



Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of _every_ node never differ by more than 1.

**Example:**

    
    
    Given the sorted linked list: [-10,-3,0,5,9],
    
    One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
    
          0
         / \
       -3   9
       /   /
     -10  5
    


**Tags:** Depth-first Search, Linked List

**Difficulty:** Medium

**思路:**
