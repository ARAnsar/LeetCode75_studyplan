class Solution(object):
    def pivotIndex(self, nums):
        nums.append(0)
        t = sum(nums)
        x = 0
        for i in range(0,len(nums)):
            t = t - nums[i]
            if t == x:
                break
            x = x + nums[i]
        if i == len(nums)-1:
            i = -1
        return i
