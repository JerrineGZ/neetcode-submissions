class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total_score = 0
        score_list = []
        score = 0
        for ops in operations:
            match ops:
                case '+':
                    score_list.append(score_list[-1] + score_list[-2])
                case 'D':
                    score_list.append(2 * score_list[-1])
                case 'C':
                    score_list.pop()
                case _:
                    score_list.append(int(ops))
        for score in score_list:
            total_score += score
        return total_score