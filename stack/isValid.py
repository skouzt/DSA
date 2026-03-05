class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_bracket = ("(", "{", "[")
        bracket_map = {')':'(', ']':'[', '}':'{'}
        for v in s:
            if v in opening_bracket:
                stack.append(v)
            elif not stack:
                return False
            elif stack[-1] == bracket_map[v]:
                stack.pop()
            else:
                return False  
        return not stack