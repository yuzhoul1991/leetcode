class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        # Sort the strings in strs in descending order in terms of length since it asks
        # for the longest length. Starting from the first keep checking until find one
        # that none of the other strings is it's subsequence

        # helper function returns if x is y's subsequence
        def is_subsequence(x, y):
            x_idx = 0
            for i in range(len(y)):
                if x_idx == len(x): break
                if y[i] == x[x_idx]:
                    x_idx += 1
            return x_idx == len(x)

        strs.sort(key=len, reverse=True)
        n = len(strs)
        for i in range(n):
            current_string = strs[i]
            is_answer = True
            for j in range(n):
                if i == j: continue
                string = strs[j]
                if is_subsequence(current_string, string):
                    is_answer = False
                    break
            if is_answer: return len(current_string)
        return -1
        
