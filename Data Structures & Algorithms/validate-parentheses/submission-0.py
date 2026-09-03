class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        previous_to_last={")":"(","]":"[","}":"{"}
        for character in s:
            if character in previous_to_last:
                if stack and stack[-1]== previous_to_last[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        return True if not stack else False
