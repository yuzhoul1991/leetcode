class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # use hash table to store letter count
        n = len(s)
        m = len(p)
        p_counter = collections.Counter(p)
        window_counter = collections.Counter(s[:m-1])
        ret = []
        # Use a sliding window from m-1 to n
        # update the window_counter on the fly
        for i in range(m-1, n):
            window_counter[s[i]] += 1
            if window_counter == p_counter:
                ret.append(i-m+1)
            window_counter[s[i-m+1]] -= 1
            if not window_counter[s[i-m+1]]: del window_counter[s[i-m+1]]

        return ret
        
