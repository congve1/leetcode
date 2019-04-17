# 网络延迟时间

## 描述

有 `N` 个网络节点，标记为 `1` 到 `N`。

给定一个列表 `times`，表示信号经过 **有向** 边的传递时间。 `times[i] = (u, v, w)`，其中 `u` 是源节点，`v` 是目标节点， `w` 是一个信号从源节点传递到目标节点的时间。

现在，我们向当前的节点 `K` 发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 `-1`。

**注意:**

  1. `N` 的范围在 `[1, 100]` 之间。
  2. `K` 的范围在 `[1, N]` 之间。
  3. `times` 的长度在 `[1, 6000]` 之间。
  4. 所有的边 `times[i] = (u, v, w)` 都有 `1 <= u, v <= N` 且 `0 <= w <= 100`。



# Network Delay Time

## Description



There are `N` network nodes, labelled `1` to `N`.

Given `times`, a list of travel times as **directed** edges `times[i] = (u, v, w)`, where `u` is the source node, `v` is the target node, and `w` is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node `K`. How long will it take for all nodes to receive the signal? If it is impossible, return `-1`.

**Note:**

  1. `N` will be in the range `[1, 100]`.
  2. `K` will be in the range `[1, N]`.
  3. The length of `times` will be in the range `[1, 6000]`.
  4. All edges `times[i] = (u, v, w)` will have `1 <= u, v <= N` and `0 <= w <= 100`.




**Tags:** Heap, Depth-first Search, Breadth-first Search, Graph

**Difficulty:** Medium

**思路:**
