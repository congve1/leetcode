# 交替位二进制数

## 描述

给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。

**示例 1:**

    
    
    **输入:** 5
    **输出:** True
    **解释:**
    5的二进制数是: 101
    

**示例 2:**

    
    
    **输入:** 7
    **输出:** False
    **解释:**
    7的二进制数是: 111
    

**示例  3:**

    
    
    **输入:** 11
    **输出:** False
    **解释:**
    11的二进制数是: 1011
    

**  示例 4:**

    
    
    **输入:** 10
    **输出:** True
    **解释:**
    10的二进制数是: 1010
    



# Binary Number with Alternating Bits

## Description



Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

**Example 1:**  

    
    

    **Input:** 5

    **Output:** True

    **Explanation:**

    The binary representation of 5 is: 101

    

**Example 2:**  

    
    

    **Input:** 7

    **Output:** False

    **Explanation:**

    The binary representation of 7 is: 111.

    

**Example 3:**  

    
    

    **Input:** 11

    **Output:** False

    **Explanation:**

    The binary representation of 11 is: 1011.

    

**Example 4:**  

    
    

    **Input:** 10

    **Output:** True

    **Explanation:**

    The binary representation of 10 is: 1010.

    


**Tags:** Bit Manipulation

**Difficulty:** Easy

**思路:**
    /*
    * 分析：
    * 如果n是交替的01，对于它右移一位后得到的m，
    * 存在n跟m在二进制下必然是0和1对应的（对位）。异或运算必定都是1；
    * 举个栗子：5=101 5>>1=10,5^(5>>1)=111 (这是伪代码)
    *  101
    *   10  =111
    * 其他情况都不会满足这个特征。所以temp=n^(n>>1)必定满足temp=2^N-1;
    * 而temp+1后是N+1位二进制数2^(N+1)。
    * 所以temp&(temp+1)==0；
    * 如果满足这个等式就是就是交替位二进制数
    */