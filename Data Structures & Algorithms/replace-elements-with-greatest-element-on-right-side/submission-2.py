class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if not arr[i+1:]:
                max_val = -1
            else:
                max_val = max(arr[i+1:])
            arr[i] = max_val
        return arr