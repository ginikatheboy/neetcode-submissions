class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        managram = {}
        
        for value in strs:
            sorted_word = "".join(sorted(value))
            
            if sorted_word not in managram:
                managram[sorted_word] = [value]
            else:
                managram[sorted_word].append(value)
                
        return list(managram.values())