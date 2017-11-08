class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        bitlen = 0
        temp = x
        while temp > 0:
            bitlen = bitlen + 1
            temp = temp // 10
        while x > 0:
            t = 10 ** (bitlen - 1)
            maxbit = x // t
            minbit = x % 10
            if maxbit != minbit:
                return False
            x = (x - t * maxbit - minbit) // 10
            bitlen = bitlen - 2
        return True

print(Solution().isPalindrome(2124444212))