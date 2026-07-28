class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0

        while l<r:
            if heights[l]>heights[r]:
                volume = (r-l)*heights[r]
                r-=1
            else:
                volume = (r-l)*heights[l]
                l+=1
            
            res = max(volume, res)
        
        return res