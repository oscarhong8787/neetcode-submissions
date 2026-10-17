class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                num = ord(char)-ord("a")
                count[num]+=1
            wordDict[tuple(count)].append(word)
        return list(wordDict.values())