class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        if len(nums) == 1 and nums[0] != target:
            return -1

        hi = len(nums)
        lo = 0
        mid = (hi + lo) // 2

        while lo < hi:
            mid = (hi + lo) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        
        return -1
                  