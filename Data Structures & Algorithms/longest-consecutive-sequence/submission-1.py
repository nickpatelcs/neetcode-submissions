class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            seen[i] = 1
        candidates = {}
        for i in nums:
            if i-1 not in seen:
                candidates[i] = 1
        count = 0
        longest = 0
        for i in candidates:
            count = 1
            while i+1 in seen:
                i += 1
                count+=1
            longest = max(count, longest)
        return longest