class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        strs = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        m = {}
        index = 1
        for s in strs:
            for ch in s:
                m[ch] = index
            index += 1
        rtn = []
        for word in words:
            word_new = str(word).lower()
            index = m[word_new[0]]
            isOneGroup = True
            for w in word_new:
                if index != m[w]:
                    isOneGroup = False
                    break
            if isOneGroup:
               rtn.append(word)
        return rtn

print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))