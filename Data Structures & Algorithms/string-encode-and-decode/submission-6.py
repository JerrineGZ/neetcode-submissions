class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "!@!"
        encoded_str = "#!@".join(strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        answer = s.split('#!@')
        if "!@!" in answer:
            return []
        return answer