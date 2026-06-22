import copy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arrs = []
        for i in range(2):
            for num in nums:
                arrs.append(num)
        return arrs