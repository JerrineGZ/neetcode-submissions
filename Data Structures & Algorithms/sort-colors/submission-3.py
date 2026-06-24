class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for i in nums:
            counts[i] += 1
        i = 0
        for k in range(3):
            for j in range(counts[k]):
                nums[i] = k
                i += 1
