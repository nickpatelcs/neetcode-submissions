class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {}
        for i in range(0, len(nums)):
            if target - nums[i] in rec:
                return [rec[target - nums[i]], i]
            rec[nums[i]] = i
         
        