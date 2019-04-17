# 骑士拨号器

## 描述

国际象棋中的骑士可以按下图所示进行移动：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/11/03/knight.png) .           ![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/11/03/keypad.png)

  
这一次，我们将 "骑士" 放在电话拨号盘的任意数字键（如上图所示）上，接下来，骑士将会跳 N-1 步。每一步必须是从一个数字键跳到另一个数字键。

每当它落在一个键上（包括骑士的初始位置），都会拨出键所对应的数字，总共按下 `N` 位数字。

你能用这种方式拨出多少个不同的号码？

因为答案可能很大， **所以输出答案模  `10^9 + 7`**。



**示例 1：**

    
    
    **输入：** 1
    **输出：** 10
    

**示例 2：**

    
    
    **输入：** 2
    **输出：** 20
    

**示例 3：**

    
    
    **输入：** 3
    **输出：** 46
    



**提示：**

  * `1 <= N <= 5000`



# Knight Dialer

## Description



A chess knight can move as indicated in the chess diagram below:

![](https://assets.leetcode.com/uploads/2018/10/12/knight.png) .           ![](https://assets.leetcode.com/uploads/2018/10/30/keypad.png)



This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes `N-1` hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing `N` digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, **output the answer  modulo `10^9 + 7`**.



**Example 1:**

    
    
    **Input:** 1
    **Output:** 10
    

**Example 2:**

    
    
    **Input:** 2
    **Output:** 20
    

**Example 3:**

    
    
    **Input:** 3
    **Output:** 46
    



**Note:**

  * `1 <= N <= 5000`


**Tags:** Dynamic Programming

**Difficulty:** Medium

**思路:**
