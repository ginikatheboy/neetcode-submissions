class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(houses):
            prev, cur = 0, 0

            for n in houses:
                prev, cur = cur, max(cur, prev + n)

            return cur

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


        