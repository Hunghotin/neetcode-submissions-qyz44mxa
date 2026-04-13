class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [0]*n
        rightmax = [0]*n
        leftmax[0] = height[0]
        rightmax[n-1] = height[n-1]
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1], height[i])
        for j in range(n-2,-1,-1):
            rightmax[j] = max(rightmax[j+1], height[j])
        result = 0
        print(leftmax, rightmax)
        for k in range(n):
            result += max(min(leftmax[k], rightmax[k])-height[k],0)
        return result