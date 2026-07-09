class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in answer:
                answer[sorted_string].append(s)
            else:
                answer[sorted_string] = [s]
        return_list = list(answer.values())
        return return_list