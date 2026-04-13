class Solution:
    def isPalindrome(self, s: str) -> bool:
        apm = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        i = 0
        j = len(s)-1
        while i<j:
            if s[i] in apm :
                if s[j] in apm:
                    if s[i].lower()==s[j].lower():
                        i+=1
                        j-=1
                    else:
                        return False
                else:
                    j-=1
            else:
                i+=1
        return True
        