class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

    #def sub_array(nums, k):
        if len(nums) < 2:
            return False
        remainder_map = {0:-1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k
            if r not in remainder_map:
                remainder_map[r] = i
            elif i - remainder_map[r] > 1:
                return True

        return False

            



        