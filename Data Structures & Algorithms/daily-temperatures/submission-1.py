class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack!=[]:
                tp = stack.pop()
                if tp[0]<temp:
                    res[tp[1]]=i-tp[1]
                else:
                    stack.append(tp)
                    stack.append([temp, i])
                    break
            else:
                stack.append([temp, i])

        return res