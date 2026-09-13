class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_helper(nums, len(nums) - 1, 0, target)
    
    def binary_helper(self, nums: List[int], hi: int, lo: int, target: int) -> int:
        if lo > hi:
            return -1

        mid = (hi + lo) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binary_helper(nums, mid - 1, lo, target)
        else:
            return self.binary_helper(nums, hi, mid + 1, target)