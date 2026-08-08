class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                product *= i
        
        result = []
        for j in range(0, len(nums)):
            curr = nums[j]
            if curr == 0 and zero_count == 1:
                result.append(product)
            elif curr != 0 and zero_count == 1:
                result.append(0)
            elif zero_count > 1:
                result.append(0)
            else:
                result.append(product // curr)
        
        return result
        



        