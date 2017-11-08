class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(numbers)):
            other = target - numbers[i]
            if other in m:
                return [m[other] + 1, i + 1]
            m[numbers[i]] = i
        return []

print(Solution().twoSum([2,7,11,15],18))