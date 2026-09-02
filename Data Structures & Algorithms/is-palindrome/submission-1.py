class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Pointers at the start and end
        l, r = 0, len(s) - 1

        while l < r:
            # 1. Skip non-alphanumeric characters from the left
            while l < r and not s[l].isalnum():
                l += 1
            
            # 2. Skip non-alphanumeric characters from the right
            while r > l and not s[r].isalnum():
                r -= 1
            
            # 3. Compare the characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            # 4. Move pointers inward
            l += 1
            r -= 1
            
        return True