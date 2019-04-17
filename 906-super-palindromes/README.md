# 超级回文数

## 描述

如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。

现在，给定两个正整数 `L` 和 `R` （以字符串形式表示），返回包含在范围 `[L, R]` 中的超级回文数的数目。



**示例：**

    
    
    **输入：** L = "4", R = "1000"
    **输出：** 4
    **解释：** 4，9，121，以及 484 是超级回文数。
    注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。



**提示：**

  1. `1 <= len(L) <= 18`
  2. `1 <= len(R) <= 18`
  3. `L` 和 `R` 是表示 `[1, 10^18)` 范围的整数的字符串。
  4. `int(L) <= int(R)`





# Super Palindromes

## Description



Let's say a positive integer is a  _superpalindrome_  if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers `L` and `R` (represented as strings), return the number of superpalindromes in the inclusive range `[L, R]`.



**Example 1:**

    
    
    **Input:** L = "4", R = "1000"
    **Output:** 4
    **Explanation** : 4, 9, 121, and 484 are superpalindromes.
    Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.



**Note:**

  1. `1 <= len(L) <= 18`
  2. `1 <= len(R) <= 18`
  3. `L` and `R` are strings representing integers in the range `[1, 10^18)`.
  4. `int(L) <= int(R)`




**Tags:** Math

**Difficulty:** Hard

**思路:**
