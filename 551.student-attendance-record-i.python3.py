class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        two_l = False
        a_count = 0
        for idx, val in enumerate(s):
            if val == 'A':
                if a_count > 0: return False
                a_count += 1
            if val == 'L':
                if two_l: return False
                if idx > 0 and s[idx-1] == 'L':
                    two_l = True
            else:
                two_l = False
        return True
