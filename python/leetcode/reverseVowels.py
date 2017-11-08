import re


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

print(Solution().reverseVowels("bae"))
print(Solution().reverseVowels("hello"))
print(Solution().reverseVowels("ela"))
print(Solution().reverseVowels("ae"))