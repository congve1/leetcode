class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = {}
        for email in emails:
            split = email.split('@')
            name = split[0]
            domain = split[1]
            name=''.join(name.split('.'))
            name = name.split('+')[0]
            email_set['@'.join([name, domain])] = email
        return len(email_set)
        