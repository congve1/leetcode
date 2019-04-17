# 蛇梯棋

## 描述

在一块 N x N 的棋盘 `board` 上， **从棋盘的左下角开始** ，每一行交替方向，按从 `1` 到 `N*N` 的数字给方格编号。例如，对于一块 6 x 6 大小的棋盘，可以编号如下：

    
    
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/31/snakes.png)
    

玩家从棋盘上的方格 `1` （总是在最后一行、第一列）开始出发。

每一次从方格 `x` 起始的移动都由以下部分组成：

  * 你选择一个目标方块 `S`，它的编号是 `x+1`，`x+2`，`x+3`，`x+4`，`x+5`，或者 `x+6`，只要这个数字 `<= N*N`。
  * 如果 `S` 有一个蛇或梯子，你就移动到那个蛇或梯子的目的地。否则，你会移动到 `S`。 

在 `r` 行 `c` 列上的方格里有 "蛇" 或 "梯子"；如果 `board[r][c] != -1`，那个蛇或梯子的目的地将会是 `board[r][c]`。

注意，你每次移动最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，你也不会继续移动。

返回达到方格 N*N 所需的最少移动次数，如果不可能，则返回 `-1`。



**示例：**

    
    
    **输入：** [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]]
    **输出：** 4
    **解释：**
    首先，从方格 1 [第 5 行，第 0 列] 开始。
    你决定移动到方格 2，并必须爬过梯子移动到到方格 15。
    然后你决定移动到方格 17 [第 3 行，第 5 列]，必须爬过蛇到方格 13。
    然后你决定移动到方格 14，且必须通过梯子移动到方格 35。
    然后你决定移动到方格 36, 游戏结束。
    可以证明你需要至少 4 次移动才能到达第 N*N 个方格，所以答案是 4。
    



**提示：**

  1. `2 <= board.length = board[0].length <= 20`
  2. `board[i][j]` 介于 `1` 和 `N*N` 之间或者等于 `-1`。
  3. 编号为 `1` 的方格上没有蛇或梯子。
  4. 编号为 `N*N` 的方格上没有蛇或梯子。



# Snakes and Ladders

## Description



On an N x N `board`, the numbers from `1` to `N*N` are written  _boustrophedonically_   **starting from the bottom  left of the board**, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:

    
    
    ![](https://assets.leetcode.com/uploads/2018/09/23/snakes.png)
    

You start on square `1` of the board (which is always in the last row and first column).  Each move, starting from square `x`, consists of the following:

  * You choose a destination square `S` with number `x+1`, `x+2`, `x+3`, `x+4`, `x+5`, or `x+6`, provided this number is `<= N*N`. 
    * (This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations.)
  * If `S` has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to `S`.

A board square on row `r` and column `c` has a "snake or ladder" if `board[r][c] != -1`.  The destination of that snake or ladder is `board[r][c]`.

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do **not** continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do **not** continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return `-1`.

**Example 1:**

    
    
    **Input:** [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]]
    **Output:** 4
    **Explanation:**
    At the beginning, you start at square 1 [at row 5, column 0].
    You decide to move to square 2, and must take the ladder to square 15.
    You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
    You then decide to move to square 14, and must take the ladder to square 35.
    You then decide to move to square 36, ending the game.
    It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
    

**Note:**

  1. `2 <= board.length = board[0].length <= 20`
  2. `board[i][j]` is between `1` and `N*N` or is equal to `-1`.
  3. The board square with number `1` has no snake or ladder.
  4. The board square with number `N*N` has no snake or ladder.


**Tags:** Breadth-first Search

**Difficulty:** Medium

**思路:**
