class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_so_far = []

        for i in nums:
            if i in nums_so_far:
                return True
            nums_so_far.append(i)

        return False
        