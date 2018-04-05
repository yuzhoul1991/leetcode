class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        use count to indicate 0 and 1, when encounter a 0 decrement, when encounter a 1
        increment the count. As we iterate the array, if the count value at two position        are the same, then between these two indices there are the same number of 1 and 0s
        Use a hash to keep track of the first time a count appears since we want the 
        longest subarray. 
        """
        # count => index
        hsh = {0 : -1}
        count = 0
        ret = 0
        for idx, val in enumerate(nums):
            if val == 0: count -= 1
            else: count += 1
            if count not in hsh: hsh[count] = idx
            else:
                ret = max(ret, idx-hsh[count])
        return ret

        
