class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        index = 0
        for num in nums:
            if num in m:
                continue
            m[num] = 1
            nums[index] = num
            index += 1
        return index

nums = [1,1,2,3,3,4,4]
print(Solution().removeDuplicates(nums))
print(nums)