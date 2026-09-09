class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums) - 1
        lo = 0

        while lo <= hi:
            mid = (hi + lo) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1
                  