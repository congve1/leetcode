# 建立四叉树

## 描述

我们想要使用一棵四叉树来储存一个 `N x N` 的布尔值网络。网络中每一格的值只会是真或假。树的根结点代表整个网络。对于每个结点, 它将被分等成四个孩子结点 **直到这个区域内的值都是相同的.**

每个结点还有另外两个布尔变量: `isLeaf` 和 `val`。`isLeaf` 当这个节点是一个叶子结点时为真。`val` 变量储存叶子结点所代表的区域的值。

你的任务是使用一个四叉树表示给定的网络。下面的例子将有助于你理解这个问题：

给定下面这个`8 x 8` 网络，我们将这样建立一个对应的四叉树：

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid.png)

由上文的定义，它能被这样分割：

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid_divided.png)



对应的四叉树应该像下面这样，每个结点由一对 `(isLeaf, val)` 所代表.

对于非叶子结点，`val` 可以是任意的，所以使用 `*` 代替。

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_quad_tree.png)

**提示：**

  1. `N` 将小于 `1000` 且确保是 2 的整次幂。
  2. 如果你想了解更多关于四叉树的知识，你可以参考这个 [wiki](https://en.wikipedia.org/wiki/Quadtree) 页面。



# Construct Quad Tree

## Description



We want to use quad trees to store an `N x N` boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes **until the values in the region it represents are all the same**.

Each node has another two boolean attributes : `isLeaf` and `val`. `isLeaf` is true if and only if the node is a leaf node. The `val` attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the `8 x 8` grid below, we want to construct the corresponding quad tree:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid.png)

It can be divided according to the definition above:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid_divided.png)



The corresponding quad tree should be as following, where each node is represented as a `(isLeaf, val)` pair.

For the non-leaf nodes, `val` can be arbitrary, so it is represented as `*`.

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_quad_tree.png)

**Note:**

  1. `N` is less than `1000` and guaranteened to be a power of 2.
  2. If you want to know more about the quad tree, you can refer to its [wiki](https://en.wikipedia.org/wiki/Quadtree).


**Tags:** 

**Difficulty:** Easy

**思路:**
