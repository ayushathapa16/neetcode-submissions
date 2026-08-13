class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        longest_length = 0
        for i in nums_set:
            if i - 1 not in nums_set:
                next = i + 1
                while next in nums_set:
                    next += 1
                longest_length = max(longest_length, next - i)
        return longest_length
        