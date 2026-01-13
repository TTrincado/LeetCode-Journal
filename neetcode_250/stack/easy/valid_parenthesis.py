class Solution:
    """
    Logic:
    1. We iterate through the string.
    2. If we see an open bracket, we push it onto the stack.
    3. If we see a close bracket:
       - Check if the stack is empty and if the top of the stack matches the corresponding opener.
       - Pop the top of the stack if match, else return False.
    4. At the end, if the stack is empty, all brackets were matched correctly.
    
    Time Complexity: O(N) - Single pass through the string.
    Space Complexity: O(N) - In worst case ,e.g. "(((((", stack grows to size N.
    """
    def isValid(self, s: str) -> bool:
        stack = []
        charmap = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in charmap:
                if stack and stack[-1] == charmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False