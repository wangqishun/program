class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rtn = 0
        for num in nums:
            rtn ^= num
        return rtn

a = [1,2,3,4,1,2,3,4,10,100,10]
print(Solution().singleNumber(a))