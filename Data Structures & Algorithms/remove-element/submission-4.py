class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = []
        for i in nums:
            if i == val:
                continue
            x.append(i)
        for i in range(len(x)):
            nums[i] = x[i]
        return len(x)
