class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                tarp= leftMax - height[l]
                if tarp > 0:
                    res += tarp
                l += 1
                leftMax = max(leftMax, height[l])
                
            else:
                tarp =  rightMax - height[r]
                if tarp > 0:
                    res += tarp
                r -= 1
                rightMax = max(rightMax, height[r])
        return res