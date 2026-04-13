class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''
        for i in digits:
            n+=str(i)
        n = int(n)
        n += 1
        n = str(n)
        res = []
        for i in n:
            res.append(i)
        return res