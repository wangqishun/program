class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        isFirstCaptial = word[0].isupper()
        captialNum = 0
        for w in word:
            if w.isupper():
                captialNum += 1
        if captialNum == 0 or (isFirstCaptial and (captialNum == 1 or captialNum == len(word))):
            return True
        return False

print(Solution().detectCapitalUse("USA"))
print(Solution().detectCapitalUse("Flag"))
print(Solution().detectCapitalUse("flag"))
print(Solution().detectCapitalUse("fLag"))
print(Solution().detectCapitalUse("FlAg"))