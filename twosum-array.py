class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            curSum = number[l] + number[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []

    #big O: O(n) time, O(1) space