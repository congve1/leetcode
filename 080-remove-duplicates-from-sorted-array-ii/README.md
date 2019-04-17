# 删除排序数组中的重复项 II

## 描述

给定一个排序数组，你需要在 **[原地](http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)** 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 **[原地](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)修改输入数组**并在使用 O(1) 额外空间的条件下完成。

**示例  1:**

    
    
    给定 _nums_ = **[1,1,1,2,2,3]** ,
    
    函数应返回新长度 length = **5** , 并且原数组的前五个元素被修改为 **1, 1, 2, 2,** **3** 。
    
    你不需要考虑数组中超出新长度后面的元素。

**示例  2:**

    
    
    给定 _nums_ = **[0,0,1,1,1,1,2,3,3]** ,
    
    函数应返回新长度 length = **7** , 并且原数组的前五个元素被修改为  **0** , **0** , **1** , **1** , **2** , **3** , **3 。**
    
    你不需要考虑数组中超出新长度后面的元素。
    

**说明:**

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以 **" 引用"**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

    
    
    // **nums** 是以"引用"方式传递的。也就是说，不对实参做任何拷贝
    int len = removeDuplicates(nums);
    
    // 在函数里修改输入数组对于调用者是可见的。
    // 根据你的函数返回的长度, 它会打印出数组中 **该长度范围内** 的所有元素。
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }



# Remove Duplicates from Sorted Array II

## Description



Given a sorted array _nums_ , remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that duplicates appeared at most  _twice_ and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Example 1:**

    
    
    Given _nums_ = **[1,1,1,2,2,3]** ,
    
    Your function should return length = **5** , with the first five elements of _nums_ being **1, 1, 2, 2** and **3** respectively.
    
    It doesn't matter what you leave beyond the returned length.

**Example 2:**

    
    
    Given _nums_ = **[0,0,1,1,1,1,2,3,3]** ,
    
    Your function should return length = **7** , with the first seven elements of _nums_ being modified to  **0** , **0** , **1** , **1** , **2** , **3** and  **3** respectively.
    
    It doesn't matter what values are set beyond the returned length.
    

**Clarification:**

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by **reference** , which means modification to the input array will be known to the caller as well.

Internally you can think of this:

    
    
    // **nums** is passed in by reference. (i.e., without making a copy)
    int len = removeDuplicates(nums);
    
    // any modification to **nums** in your function would be known by the caller.
    // using the length returned by your function, it prints the first **len** elements.
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }
    


**Tags:** Array, Two Pointers

**Difficulty:** Medium

**思路:**
