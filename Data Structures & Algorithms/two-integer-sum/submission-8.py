class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for index, num in enumerate(nums):
            goal = target - num
            if goal in check:
                index_of_goal = check.get(goal)
                return [index_of_goal, index]
            check[num] = index