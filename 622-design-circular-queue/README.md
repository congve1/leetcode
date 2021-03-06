# 设计循环队列

## 描述

设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为"环形缓冲器"。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

  * `MyCircularQueue(k)`: 构造器，设置队列长度为 k 。
  * `Front`: 从队首获取元素。如果队列为空，返回 -1 。
  * `Rear`: 获取队尾元素。如果队列为空，返回 -1 。
  * `enQueue(value)`: 向循环队列插入一个元素。如果成功插入则返回真。
  * `deQueue()`: 从循环队列中删除一个元素。如果成功删除则返回真。
  * `isEmpty()`: 检查循环队列是否为空。
  * `isFull()`: 检查循环队列是否已满。



**示例：**

    
    
    MyCircularQueue circularQueue = new MycircularQueue(3); // 设置长度为 3
    
    circularQueue.enQueue(1);  // 返回 true
    
    circularQueue.enQueue(2);  // 返回 true
    
    circularQueue.enQueue(3);  // 返回 true
    
    circularQueue.enQueue(4);  // 返回 false，队列已满
    
    circularQueue.Rear();  // 返回 3
    
    circularQueue.isFull();  // 返回 true
    
    circularQueue.deQueue();  // 返回 true
    
    circularQueue.enQueue(4);  // 返回 true
    
    circularQueue.Rear();  // 返回 4
     



**提示：**

  * 所有的值都在 0 至 1000 的范围内；
  * 操作数将在 1 至 1000 的范围内；
  * 请不要使用内置的队列库。



# Design Circular Queue

## Description



Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

  * `MyCircularQueue(k)`: Constructor, set the size of the queue to be k.
  * `Front`: Get the front item from the queue. If the queue is empty, return -1.
  * `Rear`: Get the last item from the queue. If the queue is empty, return -1.
  * `enQueue(value)`: Insert an element into the circular queue. Return true if the operation is successful.
  * `deQueue()`: Delete an element from the circular queue. Return true if the operation is successful.
  * `isEmpty()`: Checks whether the circular queue is empty or not.
  * `isFull()`: Checks whether the circular queue is full or not.



**Example:**

    
    
    MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
    circularQueue.enQueue(1);  // return true
    circularQueue.enQueue(2);  // return true
    circularQueue.enQueue(3);  // return true
    circularQueue.enQueue(4);  // return false, the queue is full
    circularQueue.Rear();  // return 3
    circularQueue.isFull();  // return true
    circularQueue.deQueue();  // return true
    circularQueue.enQueue(4);  // return true
    circularQueue.Rear();  // return 4
    



**Note:**

  * All values will be in the range of [0, 1000].
  * The number of operations will be in the range of [1, 1000].
  * Please do not use the built-in Queue library.


**Tags:** Design, Queue

**Difficulty:** Medium

**思路:**
