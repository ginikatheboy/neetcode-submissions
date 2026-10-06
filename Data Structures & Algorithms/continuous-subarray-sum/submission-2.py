class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False

        remainder = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k

            if r in remainder:
                if i - remainder[r] > 1:
                    return True
            else:
                remainder[r] = i

        return False
            



        