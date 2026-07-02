class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums) - 1
        while b <= e:
            m = (b + e) // 2
            # found the target
            if target == nums[m]:
                return m
            # explore the left half
            elif target < nums[m]:
                e = m - 1
            # explore the right half
            else:
                b = m + 1
        return -1
        