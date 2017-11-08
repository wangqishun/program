class Solution:
    def listToInt(self, x):
        if type(x) == int:
            return x
        else:
            return x[0]


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for index, i in enumerate(nums):
            if i not in num_map:
                num_map[i] = index
            else:
                num_map[i] = [num_map[i], index]

        for key, val in num_map.items():
            if target - key in num_map:
                if key == target - key:
                    return [val[0], val[1]]
                else:
                    return [self.listToInt(val), self.listToInt(num_map[target - key])]

s = Solution()
print(s.twoSum([3,3], 6))


