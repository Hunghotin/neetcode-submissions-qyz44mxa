class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range(1,len(height)-1):
            leftmax = 0
            rightmax = 0
            for j in range(0,i):
                leftmax = max(leftmax, height[j])
            for k in range(len(height)-1, i, -1):
                rightmax = max(rightmax, height[k])
            if min(leftmax, rightmax)>height[i]:
                result += min(leftmax, rightmax) - height[i]
        return result 
            