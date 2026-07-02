class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # convert nums into set
        nums_set = set(nums)

        # check whether their lengths are equal
        if len(nums_set) < len(nums):
            return True
        else:
            return False
        