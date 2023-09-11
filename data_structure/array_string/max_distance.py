
class Solution:
    def maxDistance(self, nums):
        if len(nums) < 2:
            return 0

        maxDis = 0
        for i in range(len(nums)-1):
            currenDis = nums[i+1] - nums[i]

            maxDis = max(maxDis,currenDis)
        return maxDis






nums = [3,0,2,1]
print(Solution().maxDistance(nums))   
