# Range 模块

## 描述

Range 模块是跟踪数字范围的模块。你的任务是以一种有效的方式设计和实现以下接口。

  * `addRange(int left, int right)` 添加半开区间 `[left, right)`，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 `[left, right)` 中尚未跟踪的任何数字到该区间中。
  * `queryRange(int left, int right)` 只有在当前正在跟踪区间 `[left, right)` 中的每一个实数时，才返回 true。
  * `removeRange(int left, int right)` 停止跟踪区间 `[left, right)` 中当前正在跟踪的每个实数。



**示例：**

    
    
    **addRange(10, 20)** : null
    **removeRange(14, 16)** : null
    **queryRange(10, 14)** : true （区间 [10, 14) 中的每个数都正在被跟踪）
    **queryRange(13, 15)** : false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
    **queryRange(16, 17)** : true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
    



**提示：**

  * 半开区间 `[left, right)` 表示所有满足 `left <= x < right` 的实数。
  * 对 `addRange, queryRange, removeRange` 的所有调用中 `0 < left < right < 10^9`。
  * 在单个测试用例中，对 `addRange` 的调用总数不超过 `1000` 次。
  * 在单个测试用例中，对  `queryRange` 的调用总数不超过 `5000` 次。
  * 在单个测试用例中，对 `removeRange` 的调用总数不超过 `1000` 次。





# Range Module

## Description



A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

* `addRange(int left, int right)` Adds the half-open interval `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.

* `queryRange(int left, int right)` Returns true if and only if every real number in the interval `[left, right)` is currently being tracked.

* `removeRange(int left, int right)` Stops tracking every real number currently being tracked in the interval `[left, right)`.

**Example 1:**  

    
    
    **addRange(10, 20)** : null
    **removeRange(14, 16)** : null
    **queryRange(10, 14)** : true (Every number in [10, 14) is being tracked)
    **queryRange(13, 15)** : false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
    **queryRange(16, 17)** : true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
    

**Note:**

* A half open interval `[left, right)` denotes all real numbers `left <= x < right`.
* `0 < left < right < 10^9` in all calls to `addRange, queryRange, removeRange`.
* The total number of calls to `addRange` in a single test case is at most `1000`.
* The total number of calls to `queryRange` in a single test case is at most `5000`.
* The total number of calls to `removeRange` in a single test case is at most `1000`.


**Tags:** Segment Tree, Binary Search Tree, Array

**Difficulty:** Hard

**思路:**
