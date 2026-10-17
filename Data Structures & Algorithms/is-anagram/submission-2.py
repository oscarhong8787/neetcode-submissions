class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words = {}
        for i in s:
            if i in words:
                words[i] +=1
            else:
                words[i] = 1
        for i in t:
            if i not in words or words[i]==0:
                return False
            else:
                words[i]-=1
        for i in words:
            if words[i] != 0:
                return False
        return True
        