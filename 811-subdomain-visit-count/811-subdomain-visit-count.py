class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = collections.defaultdict(int)
        for cpdomain in cpdomains:
            splits = cpdomain.split()
            count = int(splits[0])
            domains = splits[1].split('.')
            for i in range(-1,-len(domains)-1, -1):
                counts['.'.join(domains[i:])] += count
        res = []
        for k, v in counts.items():
            res.append(' '.join([str(v), k]))
        return res
        