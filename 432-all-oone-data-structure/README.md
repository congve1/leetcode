# 全 O(1) 的数据结构

## 描述

实现一个数据结构支持以下操作：

  1. Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
  2. Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否者使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。
  3. GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串`""`。
  4. GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串`""`。

挑战：以 O(1) 的时间复杂度实现所有操作。



# All O`one Data Structure

## Description



Implement a data structure supporting the following operations:

  1. Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by 1. Key is guaranteed to be a **non-empty** string.
  2. Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a **non-empty** string.
  3. GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string `""`.
  4. GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string `""`.

Challenge: Perform all these in O(1) time complexity.


**Tags:** Design

**Difficulty:** Hard

**思路:**
