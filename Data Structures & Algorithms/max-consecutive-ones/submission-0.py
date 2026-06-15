class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        res = 0
        for i in nums:
            if i == 1:
                max_consecutive_ones += 1
            if i == 0:
                max_consecutive_ones = 0
            if res < max_consecutive_ones:
                res = max_consecutive_ones
        return res   