# 字母大小写全排列

## 描述

给定一个字符串`S`，通过将字符串`S`中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

    
    
    **示例:**
    **输入:** S = "a1b2"
    **输出:** ["a1b2", "a1B2", "A1b2", "A1B2"]
    
    **输入:** S = "3z4"
    **输出:** ["3z4", "3Z4"]
    
    **输入:** S = "12345"
    **输出:** ["12345"]
    

**注意：**

  * `S` 的长度不超过`12`。
  * `S` 仅由数字和字母组成。



# Letter Case Permutation

## Description



Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

    
    

    **Examples:**

    **Input:** S = "a1b2"

    **Output:** ["a1b2", "a1B2", "A1b2", "A1B2"]

    

    **Input:** S = "3z4"

    **Output:** ["3z4", "3Z4"]

    

    **Input:** S = "12345"

    **Output:** ["12345"]

    

**Note:**

  * `S` will be a string with length between `1` and `12`.
  * `S` will consist only of letters or digits.


**Tags:** Bit Manipulation, Backtracking

**Difficulty:** Easy

**思路:**
DFS回溯：说对于每个元素都先考虑放它的情况，再考虑不放它的情况
BitMap Bitmap法，字符串S的长度为l， 则总共会有 2** l种结果，换成二进制就是0 ~ 2 **l - 1个数，对于每个数，如果某个位上是0， 就放小写；是1， 就放大写。