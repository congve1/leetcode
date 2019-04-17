# 特殊等价字符串组

## 描述

你将得到一个字符串数组 `A`。

如果经过任意次数的移动，S == T，那么两个字符串 `S` 和 `T` 是 _特殊等价_ 的。



一次 _移动_ 包括选择两个索引 `i` 和 `j`，且 `i％2 == j％2`，并且交换 `S[j]` 和 `S [i]`。

现在规定， _`A` 中的特殊等价字符串组_是 `A` 的非空子集 `S`，这样不在 `S` 中的任何字符串与 `S` 中的任何字符串都不是特殊等价的。



返回 `A` 中特殊等价字符串组的数量。



**示例 1：**

    
    
    **输入：** ["a","b","c","a","c","c"]
    **输出：** 3
    **解释：** 3 **** 组 ["a","a"]，["b"]，["c","c","c"]
    

**示例 2：**

    
    
    **输入：** ["aa","bb","ab","ba"]
    **输出：** 4
    **解释：** 4 组 ["aa"]，["bb"]，["ab"]，["ba"]
    

**示例 3：**

    
    
    **输入：** ["abc","acb","bac","bca","cab","cba"]
    **输出：** 3
    **解释：** 3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
    

**示例 4：**

    
    
    **输入：** ["abcd","cdab","adcb","cbad"]
    **输出：** 1
    **解释：** 1 组 ["abcd","cdab","adcb","cbad"]
    



**提示：**

  * `1 <= A.length <= 1000`
  * `1 <= A[i].length <= 20`
  * 所有 `A[i]` 都具有相同的长度。
  * 所有 `A[i]` 都只由小写字母组成。



# Groups of Special-Equivalent Strings

## Description



You are given an array `A` of strings.

Two strings `S` and `T` are  _special-equivalent_  if after any number of _moves_ , S == T.

A _move_ consists of choosing two indices `i` and `j` with `i % 2 == j % 2`, and swapping `S[i]` with `S[j]`.

Now, a _group of special-equivalent strings from`A`_ is a non-empty subset S of `A` such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from `A`.



**Example 1:**

    
    
    **Input:** ["a","b","c","a","c","c"]
    **Output:** 3
    **Explanation** : 3 groups ["a","a"], ["b"], ["c","c","c"]
    

**Example 2:**

    
    
    **Input:** ["aa","bb","ab","ba"]
    **Output:** 4
    **Explanation** : 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
    

**Example 3:**

    
    
    **Input:** ["abc","acb","bac","bca","cab","cba"]
    **Output:** 3
    **Explanation** : 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]
    

**Example 4:**

    
    
    **Input:** ["abcd","cdab","adcb","cbad"]
    **Output:** 1
    **Explanation** : 1 group ["abcd","cdab","adcb","cbad"]
    



**Note:**

  * `1 <= A.length <= 1000`
  * `1 <= A[i].length <= 20`
  * All `A[i]` have the same length.
  * All `A[i]` consist of only lowercase letters.


**Tags:** String

**Difficulty:** Easy

**思路:**
