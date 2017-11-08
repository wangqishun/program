class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        insert_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_index] = nums[i]
                insert_index += 1

        while insert_index < len(nums):
            nums[insert_index] = 0
            insert_index += 1

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)