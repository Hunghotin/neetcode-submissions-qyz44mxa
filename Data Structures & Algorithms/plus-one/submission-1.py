class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        for i in range(len(digits)-1,-1,-1):
            if flag:
                tmp = digits[i]+1
                flag = False
                if tmp>=10:
                    flag=True
                    digits[i] = tmp%10
                else:
                    digits[i] = tmp
                if i==0 and flag:
                    digits.insert(0,1)
        return digits
