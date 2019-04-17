# TinyURL 的加密与解密

## 描述

TinyURL是一种URL简化服务， 比如：当你输入一个URL `https://leetcode.com/problems/design-tinyurl` 时，它将返回一个简化的URL `http://tinyurl.com/4e9iAk`.

要求：设计一个 TinyURL 的加密 `encode` 和解密 `decode` 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。



# Encode and Decode TinyURL

## Description



> Note: This is a companion problem to the [System Design](https://leetcode.com/discuss/interview-question/system-design/) problem: [Design TinyURL](https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-\(-TinyURL-\)-System/).

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`.

Design the `encode` and `decode` methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


**Tags:** Hash Table, Math

**Difficulty:** Medium

**思路:**
