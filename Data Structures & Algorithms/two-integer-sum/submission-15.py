class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary
        mapping = {}

        # Create a mapping between the number in nums and its index
        for (j, num) in enumerate(nums):
            other_half = target - num

            if other_half in mapping:
                # Retrieve the index of one of the numbers
                i = mapping[other_half]
                return [i, j]
            
            # if other_half doesn't exist in mapping, then add number and its index
            mapping[num] = j
                
                    




        