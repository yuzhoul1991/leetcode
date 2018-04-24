class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # For each word, produce a mask from it's chars
        # use a hash to record the longest word length for each unique mask
        # get the max of two pair multiply across all unique masks

        # unique mask => length
        hsh = collections.defaultdict(int)
        for word in words:
            char_set = set(word)
            mask = 0
            for char in char_set:
                mask |= 1 << (ord(char) - ord('a'))
            hsh[mask] = max(hsh[mask], len(word))
        ret = 0
        for x in hsh:
            for y in hsh:
                # if x & y == 0 then no char are the same in the words they
                # represent
                if x & y == 0:
                    ret = max(ret, hsh[x] * hsh[y])
        return ret
        
