class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            sum = numbers[lo] + numbers[hi]
            if sum > target:
                hi -= 1
            elif sum < target:
                lo += 1
            else:
                return [lo + 1, hi + 1]

            

        