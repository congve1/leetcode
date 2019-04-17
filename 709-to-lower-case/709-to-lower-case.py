class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        mapping = {uppercase[i]: lowercase[i] for i in range(len(lowercase)) }
        letters = []
        for s in str:
            letters.append(s if s not in mapping else mapping[s])
        return ''.join(letters)
        