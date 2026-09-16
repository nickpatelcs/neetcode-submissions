class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = {}
        val = []
        for i in range(len(numbers)):
            numSet[numbers[i]] = i + 1
        for i in range(len(numbers)):
            if target - numbers[i] in numSet and i + 1 != numSet[target - numbers[i]]:
                val1 = max(i + 1, numSet[target - numbers[i]])
                val2 = min(i + 1, numSet[target - numbers[i]])
                val = [val2, val1]
        return val
        