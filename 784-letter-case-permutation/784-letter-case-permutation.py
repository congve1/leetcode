class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        """
        dfs
        res = []
        l = len(S)
        if l == 0:
            return ['']
        
        def dfs(start, temp):
            if start >= l or len(temp) == l:
                res.append(temp)
                return 
            if S[start].isdigit():
                dfs(start+1, temp+S[start])
            elif S[start].islower():
                dfs(start+1, temp+S[start])
                dfs(start+1, temp+S[start].upper())
            elif S[start].isupper():
                dfs(start+1, temp+S[start])
                dfs(start+1, temp+S[start].lower())
        dfs(0,"")
        return res
        """
        l = len(S)
        n = 1 << l
        res = []
        if l == 0:
            return ['']
        for i in range(n):
            temp = ''
            for j in range(l):
                if (1<<j) & i == 0:
                    temp += S[j].lower()
                else:
                    temp += S[j].upper()
            if temp not in res:
                res.append(temp)
                
        return res