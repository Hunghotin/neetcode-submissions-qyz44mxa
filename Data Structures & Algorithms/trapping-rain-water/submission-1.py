class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        i = 0
        j = len(height)-1
        leftmax = height[i]
        rightmax = height[j]
        while i<j:
            if leftmax>rightmax:
                j-=1
                rightmax = max(rightmax, height[j])
                result += rightmax-height[j]
            else:
                i+=1
                leftmax = max(leftmax, height[i])
                result += leftmax-height[i]
        
        return result

