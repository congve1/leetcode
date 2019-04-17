# 贴纸拼词

## 描述

我们给出了 N 种不同类型的贴纸。每个贴纸上都有一个小写的英文单词。

你希望从自己的贴纸集合中裁剪单个字母并重新排列它们，从而拼写出给定的目标字符串 `target`。

如果你愿意的话，你可以不止一次地使用每一张贴纸，而且每一张贴纸的数量都是无限的。

拼出目标 `target` 所需的最小贴纸数量是多少？如果任务不可能，则返回 -1。



**示例 1：**

输入：

    
    
    ["with", "example", "science"], "thehat"
    

输出：

    
    
    3
    

解释：

    
    
    我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
    把贴纸上的字母剪下来并重新排列后，就可以形成目标 "thehat" 了。
    此外，这是形成目标字符串所需的最小贴纸数量。
    

**示例 2：**

输入：

    
    
    ["notice", "possible"], "basicbasic"
    

输出：

    
    
    -1
    

解释：

    
    
    我们不能通过剪切给定贴纸的字母来形成目标"basicbasic"。
    



**提示：**

  * `stickers` 长度范围是 `[1, 50]`。
  * `stickers` 由小写英文单词组成（不带撇号）。
  * `target` 的长度在 `[1, 15]` 范围内，由小写字母组成。
  * 在所有的测试案例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选取的，目标是两个随机单词的串联。
  * 时间限制可能比平时更具挑战性。预计 50 个贴纸的测试案例平均可在35ms内解决。





# Stickers to Spell Word

## Description



We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given `target` string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the `target`? If the task is impossible, return -1.

**Example 1:**

Input:

    
    
    ["with", "example", "science"], "thehat"
    

Output:

    
    
    3
    

Explanation:

    
    
    We can use 2 "with" stickers, and 1 "example" sticker.
    After cutting and rearrange the letters of those stickers, we can form the target "thehat".
    Also, this is the minimum number of stickers necessary to form the target string.
    

**Example 2:**

Input:

    
    
    ["notice", "possible"], "basicbasic"
    

Output:

    
    
    -1
    

Explanation:

    
    
    We can't form the target "basicbasic" from cutting letters from the given stickers.
    

**Note:**

* `stickers` has length in the range `[1, 50]`.
* `stickers` consists of lowercase English words (without apostrophes).
* `target` has length in the range `[1, 15]`, and consists of lowercase English letters.
* In all test cases, all words were chosen _randomly_ from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
* The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.


**Tags:** Dynamic Programming, Backtracking

**Difficulty:** Hard

**思路:**
