class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Convert list nums into set
        nums_set = set(nums)

        # Check for duplicates
        if len(nums) > len(nums_set):
            return True

        return False
        # if len(nums) <= 1:
        #     return False

        # my_dict = {}

        # for i in nums:
        #     if i in my_dict:
        #         return True
        #     my_dict[i] = 1
        # return False
        