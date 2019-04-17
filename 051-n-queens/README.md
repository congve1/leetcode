# N皇后

## 描述

_n  _皇后问题研究的是如何将 _n_  个皇后放置在 _n_ × _n_ 的棋盘上，并且使皇后彼此之间不能相互攻击。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png)

上图为 8 皇后问题的一种解法。

给定一个整数 _n_ ，返回所有不同的  _n  _皇后问题的解决方案。

每一种解法包含一个明确的  _n_ 皇后问题的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

**示例:**

    
    
    **输入:** 4
    **输出:** [
     [".Q..",  // 解法 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // 解法 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    **解释:** 4 皇后问题存在两个不同的解法。
    



# N-Queens

## Description



The _n_ -queens puzzle is the problem of placing _n_ queens on an _n_ × _n_ chessboard such that no two queens attack each other.

![](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer _n_ , return all distinct solutions to the _n_ -queens puzzle.

Each solution contains a distinct board configuration of the _n_ -queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.

**Example:**

    
    
    **Input:** 4
    **Output:** [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    **Explanation:** There exist two distinct solutions to the 4-queens puzzle as shown above.
    


**Tags:** Backtracking

**Difficulty:** Hard

**思路:**
