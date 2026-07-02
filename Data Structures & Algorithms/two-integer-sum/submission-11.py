class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cands = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in cands:
                j = cands[diff]
                if j != i:
                    return [j, i]
            else:
                cands[nums[i]] = i
        