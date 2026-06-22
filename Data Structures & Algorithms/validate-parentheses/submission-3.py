class Solution:
    def isValid(self, s: str) -> bool:
        checker = []
        for string in s:
            if string in '({[':
                checker.append(string)
            elif string in ')}]':
                if len(checker) > 0:
                    last_bracket = checker[-1]
                    if last_bracket == '(' and string == ')':
                        checker.pop()
                    elif last_bracket == '[' and string == ']':
                        checker.pop()
                    elif last_bracket == '{' and string == '}':
                        checker.pop()
                    else:
                        checker.append(string)
                else:
                    checker.append(string)
            else:
                checker.append(string)
        return len(checker) == 0
        