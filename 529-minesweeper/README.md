# 扫雷游戏

## 描述

让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。  **' M'** 代表一个 **未挖出的** 地雷， **' E'** 代表一个 **未挖出的** 空方块， **' B' **代表没有相邻（上，下，左，右，和所有4个对角线）地雷的 **已挖出的** 空白方块， **数字** （'1' 到 '8'）表示有多少地雷与这块 **已挖出的** 方块相邻， **' X'** 则表示一个 **已挖出的** 地雷。

现在给出在所有 **未挖出的** 方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

  1. 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为  **' X'**。
  2. 如果一个 **没有相邻地雷** 的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
  3. 如果一个 **至少与一个地雷相邻** 的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
  4. 如果在此次点击中，若无更多方块可被揭露，则返回面板。



**示例 1：**

    
    
    **输入:** 
    
    [['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'M', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E']]
    
    Click : [3,0]
    
    **输出:** 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    **解释:**
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/minesweeper_example_1.png)
    

**示例 2：**

    
    
    **输入:** 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    Click : [1,2]
    
    **输出:** 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'X', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    **解释:**
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/minesweeper_example_2.png)
    



**注意：**

  1. 输入矩阵的宽和高的范围为 [1,50]。
  2. 点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。
  3. 输入面板不会是游戏结束的状态（即有地雷已被挖出）。
  4. 简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。



# Minesweeper

## Description



Let's play the minesweeper game ([Wikipedia](https://en.wikipedia.org/wiki/Minesweeper_\(video_game\)), [online game](http://minesweeperonline.com))!

You are given a 2D char matrix representing the game board. **' M'** represents an **unrevealed** mine, **' E'** represents an **unrevealed** empty square, **' B'** represents a **revealed** blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, **digit** ('1' to '8') represents how many mines are adjacent to this **revealed** square, and finally **' X'** represents a **revealed** mine.

Now given the next click position (row and column indices) among all the **unrevealed** squares ('M' or 'E'), return the board after revealing this position according to the following rules:

  1. If a mine ('M') is revealed, then the game is over - change it to **' X'**.
  2. If an empty square ('E') with **no adjacent mines** is revealed, then change it to revealed blank ('B') and all of its adjacent **unrevealed** squares should be revealed recursively.
  3. If an empty square ('E') with **at least one adjacent mine** is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
  4. Return the board when no more squares will be revealed.



**Example 1:**

    
    
    **Input:** 
    
    [['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'M', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E']]
    
    Click : [3,0]
    
    **Output:** 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    **Explanation:**
    ![](https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_1.png)
    

**Example 2:**

    
    
    **Input:** 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    Click : [1,2]
    
    **Output:** 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'X', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    **Explanation:**
    ![](https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_2.png)
    



**Note:**

  1. The range of the input matrix's height and width is [1,50].
  2. The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
  3. The input board won't be a stage when game is over (some mines have been revealed).
  4. For simplicity, not mentioned rules should be ignored in this problem. For example, you **don 't** need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.


**Tags:** Depth-first Search, Breadth-first Search

**Difficulty:** Medium

**思路:**
