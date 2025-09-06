class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(':')', '{':'}', '[':']'}
        for symbol in s:
            if symbol in parentheses:
                stack.append(symbol)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if parentheses[top] != symbol:
                    return False
        if len(stack) != 0:
            return False
        return True