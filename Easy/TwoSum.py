class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            

        for i in range(len(nums)):
            if nums[i] + nums[i+1] == target:
                return [i, i+1]