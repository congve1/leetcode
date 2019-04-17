class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = 'qwertyuiop'
        second = 'asdfghjkl'
        third = 'zxcvbnm'
        res = []
        for word in words:
            if all([c in first for c in word.lower()]) or \
               all([c in second for c in word.lower()]) or \
               all([c in third for c in word.lower()]):
                res.append(word)
                continue
        return res
            
        