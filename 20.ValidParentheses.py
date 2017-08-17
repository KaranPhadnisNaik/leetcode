class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        for ch in s:
            if ch in brackets.values():
                stack.append(ch)
            elif ch in brackets.keys():
                if stack == [] or  stack[len(stack)-1]!= brackets[ch]:
                    return False
                stack.pop()
            else:
                return False
        return stack == []
