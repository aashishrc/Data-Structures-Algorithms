class Solution:
    def isValid(self, st: str) -> bool:
        s = []
        for i in st:
            if i == ')':
                if s and s[-1] == '(':
                    s.pop()
                else:
                    return False
            elif i == '}':    
                if s and s[-1] == '{':    
                    s.pop()
                else:
                    return False
            elif i == ']':
                if s and s[-1] == '[':
                    s.pop()
                else:
                    return False
            else:
                s.append(i)
        if len(s) == 0:
            return True
        return False
            