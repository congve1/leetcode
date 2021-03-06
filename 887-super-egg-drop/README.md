# 鸡蛋掉落

## 描述

你将获得 `K` 个鸡蛋，并可以使用一栋从 `1` 到 `N`  共有 `N` 层楼的建筑。

每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

你知道存在楼层 `F` ，满足 `0 <= F <= N` 任何从高于 `F` 的楼层落下的鸡蛋都会碎，从 `F` 楼层或比它低的楼层落下的鸡蛋都不会破。

每次 _移动_ ，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 `X` 扔下（满足 `1 <= X <= N`）。

你的目标是 **确切地** 知道 `F` 的值是多少。

无论 `F` 的初始值如何，你确定 `F` 的值的最小移动次数是多少？



**示例 1：**

    
    
    **输入：** K = 1, N = 2
    **输出：** 2
    **解释：**
    鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
    否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
    如果它没碎，那么我们肯定知道 F = 2 。
    因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
    

**示例 2：**

    
    
    **输入：** K = 2, N = 6
    **输出：** 3
    

**示例 3：**

    
    
    **输入：** K = 3, N = 14
    **输出：** 4
    



**提示：**

  1. `1 <= K <= 100`
  2. `1 <= N <= 10000`



# Super Egg Drop

## Description



You are given `K` eggs, and you have access to a building with `N` floors from `1` to `N`.

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor `F` with `0 <= F <= N` such that any egg dropped at a floor higher than `F` will break, and any egg dropped at or below floor `F` will not break.

Each _move_ , you may take an egg (if you have an unbroken one) and drop it from any floor `X` (with `1 <= X <= N`).

Your goal is to know  **with certainty**  what the value of `F` is.

What is the minimum number of moves that you need to know with certainty what `F` is, regardless of the initial value of `F`?



**Example 1:**

    
    
    **Input:** K = 1, N = 2
    **Output:** 2
    **Explanation:**
    Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
    Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
    If it didn't break, then we know with certainty F = 2.
    Hence, we needed 2 moves in the worst case to know what F is with certainty.
    

**Example 2:**

    
    
    **Input:** K = 2, N = 6
    **Output:** 3
    

**Example 3:**

    
    
    **Input:** K = 3, N = 14
    **Output:** 4
    



**Note:**

  1. `1 <= K <= 100`
  2. `1 <= N <= 10000`


**Tags:** Math, Binary Search, Dynamic Programming

**Difficulty:** Hard

**思路:**
