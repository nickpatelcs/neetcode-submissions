class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {}
        for i in range(0, len(nums)):
            num = nums[i]
            num2 = target - num
            if num2 in rec:
                return [rec[num2], i]
            rec[num] = i
         
        