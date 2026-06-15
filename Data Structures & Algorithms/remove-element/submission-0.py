class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        x = []
        for i in nums:
            if i != val:
                k += 1
                x.append(i)
        for i in range(len(x)):
            nums[i] = x[i]
        return len(x)