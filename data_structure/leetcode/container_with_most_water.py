class Solution:
    def maxArea(self, height: list[int]) -> int:
        res: int = 0
        left = 0
        right = len(height) - 1


        while(left < right):
            w:int = right - left
            
            h:int = min(height[left], height[right])
            area:int = h * w
            res = max(res, area)
            if height[left] < height[right]:
                left = left + 1
            elif height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
                right = right + 1        


        return res

print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))        