class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index

nums = [3,2,2,2,3]
print(Solution().removeElement(nums, 2))
print(nums)