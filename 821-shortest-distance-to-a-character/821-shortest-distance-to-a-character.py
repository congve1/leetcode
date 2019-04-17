class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        len_s = len(S)
        e_s = []
        for i in range(len_s):
            if S[i] == C:
                e_s.append(i)
        
        res = []
        for i in range(len_s):
            #print(e_s)
            #min_d = 200000
            ds = [abs(i-e) for e in e_s]
            res.append(min(ds))
        return res
            