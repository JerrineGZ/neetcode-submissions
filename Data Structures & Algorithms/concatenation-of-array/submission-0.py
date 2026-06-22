import copy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arrs = []
        arrs = copy.deepcopy(nums)
        for x in nums:
            arrs.append(x)
        return arrs
