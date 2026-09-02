class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for char in s:
            countS[char] = 1 + countS.get(char, 0)
        
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        return countS == countT