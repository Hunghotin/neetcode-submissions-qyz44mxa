class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        i = 0
        j = len(heights)-1
        while i<j:
            a = heights[i]
            b = heights[j]
            result = max(result, min(a,b)*(j-i))
            if a == min(a,b):
                i+=1
            else:
                j-=1
        return result