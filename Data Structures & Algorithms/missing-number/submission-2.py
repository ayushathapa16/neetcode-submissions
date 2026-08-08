class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)

        n = len(nums)

        for i in range(0, n + 1):
            if i == n:
                return i
            if nums_sorted[i] != i:
                return i
        