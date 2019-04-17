# 由斜杠划分区域

## 描述

在由 1 x 1 方格组成的 N x N 网格 `grid` 中，每个 1 x 1 方块由 `/`、`\` 或空格构成。这些字符会将方块划分为一些共边的区域。

（请注意，反斜杠字符是转义的，因此 `\` 用 `"\\"` 表示。）。

返回区域的数目。



**示例 1：**

    
    
    **输入：** [
      " /",
      "/ "
    ]
    **输出：** 2
    **解释：** 2x2 网格如下：
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/1.png)

**示例 2：**

    
    
    **输入：** [
      " /",
      "  "
    ]
    **输出：** 1
    **解释：** 2x2 网格如下：
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/2.png)

**示例 3：**

    
    
    **输入：** [
      "\\/",
      "/\\"
    ]
    **输出：** 4
    **解释：** （回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
    2x2 网格如下：
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/3.png)

**示例 4：**

    
    
    **输入：** [
      "/\\",
      "\\/"
    ]
    **输出：** 5
    **解释：** （回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
    2x2 网格如下：
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/4.png)

**示例 5：**

    
    
    **输入：** [
      "//",
      "/ "
    ]
    **输出：** 3
    **解释：** 2x2 网格如下：
    ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/5.png)
    



**提示：**

  1. `1 <= grid.length == grid[0].length <= 30`
  2. `grid[i][j]` 是 `'/'`、`'\'`、或 `' '`。



# Regions Cut By Slashes

## Description



In a N x N `grid` composed of 1 x 1 squares, each 1 x 1 square consists of a `/`, `\`, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a `\` is represented as `"\\"`.)

Return the number of regions.



**Example 1:**

    
    
    **Input:** [
      " /",
      "/ "
    ]
    **Output:** 2
    **Explanation:** The 2x2 grid is as follows:
    ![](https://assets.leetcode.com/uploads/2018/12/15/1.png)
    

**Example 2:**

    
    
    **Input:** [
      " /",
      "  "
    ]
    **Output:** 1
    **Explanation:** The 2x2 grid is as follows:
    ![](https://assets.leetcode.com/uploads/2018/12/15/2.png)
    

**Example 3:**

    
    
    **Input:** [
      "\\/",
      "/\\"
    ]
    **Output:** 4
    **Explanation:** (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
    The 2x2 grid is as follows:
    ![](https://assets.leetcode.com/uploads/2018/12/15/3.png)
    

**Example 4:**

    
    
    **Input:** [
      "/\\",
      "\\/"
    ]
    **Output:** 5
    **Explanation:** (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
    The 2x2 grid is as follows:
    ![](https://assets.leetcode.com/uploads/2018/12/15/4.png)
    

**Example 5:**

    
    
    **Input:** [
      "//",
      "/ "
    ]
    **Output:** 3
    **Explanation:** The 2x2 grid is as follows:
    ![](https://assets.leetcode.com/uploads/2018/12/15/5.png)
    



**Note:**

  1. `1 <= grid.length == grid[0].length <= 30`
  2. `grid[i][j]` is either `'/'`, `'\'`, or `' '`.


**Tags:** Depth-first Search, Union Find, Graph

**Difficulty:** Medium

**思路:**
