class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(':")",'[':']','{':'}'}
        stack = []

        for i in range(len(s)):
            if s[i] in match.keys():
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                else:
                    if match[stack.pop()]!=s[i]:
                        return False
        if len(stack)!=0:
            return False

        return True
