# 单词替换

## 描述

在英语中，我们有一个叫做 `词根`(root)的概念，它可以跟着其他一些词组成另一个较长的单词----我们称这个词为 `继承词`(successor)。例如，词根`an`，跟随着单词 `other`(其他)，可以形成新的单词 `another`(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有`继承词`用`词根`替换掉。如果`继承词`有许多可以形成它的`词根`，则用最短的词根替换它。

你需要输出替换之后的句子。

**示例 1:**

    
    
    **输入:** dict(词典) = ["cat", "bat", "rat"]
    sentence(句子) = "the cattle was rattled by the battery"
    **输出:** "the cat was rat by the bat"
    

**注:**

  1. 输入只包含小写字母。
  2. 1 <= 字典单词数 <=1000
  3. 1 <=  句中词语数 <= 1000
  4. 1 <= 词根长度 <= 100
  5. 1 <= 句中词语长度 <= 1000



# Replace Words

## Description



In English, we have a concept called `root`, which can be followed by some other words to form another longer word - let's call this word `successor`. For example, the root `an`, followed by `other`, which can form another word `another`.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the `successor` in the sentence with the `root` forming it. If a `successor` has many `roots` can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

**Example 1:**

    
    
    **Input:** dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    **Output:** "the cat was rat by the bat"
    



**Note:**

  1. The input will only have lower-case letters.
  2. 1 <= dict words number <= 1000
  3. 1 <= sentence words number <= 1000
  4. 1 <= root length <= 100
  5. 1 <= sentence words length <= 1000




**Tags:** Trie, Hash Table

**Difficulty:** Medium

**思路:**
