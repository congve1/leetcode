# 复数乘法

## 描述

给定两个表示[复数](https://baike.baidu.com/item/%E5%A4%8D%E6%95%B0/254365?fr=aladdin)的字符串。

返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。

**示例 1:**

    
    
    **输入:** "1+1i", "1+1i"
    **输出:** "0+2i"
    **解释:** (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
    

**示例 2:**

    
    
    **输入:** "1+-1i", "1+-1i"
    **输出:** "0+-2i"
    **解释:** (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 
    

**注意:**

  1. 输入字符串不包含额外的空格。
  2. 输入字符串将以  **a+bi** 的形式给出，其中整数 **a** 和 **b** 的范围均在 [-100, 100] 之间。 **输出也应当符合这种形式** 。



# Complex Number Multiplication

## Description



Given two strings representing two [complex numbers](https://en.wikipedia.org/wiki/Complex_number).

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

**Example 1:**  

    
    
    **Input:** "1+1i", "1+1i"
    **Output:** "0+2i"
    **Explanation:** (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
    

**Example 2:**  

    
    
    **Input:** "1+-1i", "1+-1i"
    **Output:** "0+-2i"
    **Explanation:** (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
    

**Note:**

  1. The input strings will not have extra blank.
  2. The input strings will be given in the form of **a+bi** , where the integer **a** and **b** will both belong to the range of [-100, 100]. And **the output should be also in this form**.


**Tags:** Math, String

**Difficulty:** Medium

**思路:**
