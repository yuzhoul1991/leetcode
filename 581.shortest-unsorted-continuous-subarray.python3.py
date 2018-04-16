class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_list = sorted(nums[:])
        left, right = 0, len(nums)-1
        for left in range(len(nums)):
            if nums[left] != sorted_list[left]:
                break
            else:
                left += 1
        for right in range(len(nums)-1, 0, -1):
            if nums[right] != sorted_list[right]:
                break
            else:
                right -= 1
        if left != len(nums)-1 and right != 0:
            return right - left + 1
        else:
            return 0
