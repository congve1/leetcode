import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mose = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        counts = set()
        for word in words:
            res = ''.join([mose[ord(c)-ord('a')] for c in word])
            counts.add(res)
        return len(counts)
        