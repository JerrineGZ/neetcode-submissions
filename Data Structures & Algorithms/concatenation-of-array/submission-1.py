import copy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arrs1 = []
        arrs2 = []
        for x in nums:
            arrs1.append(x)
            arrs2.append(x)
        arrs = arrs1 + arrs2
        return arrs
