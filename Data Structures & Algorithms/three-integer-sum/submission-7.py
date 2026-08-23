class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)

        checked = set()
        result = []
        for i in range(0, len(nums_sorted)):
            element = nums_sorted[i]

            if element in checked:
                continue
            else:
                checked.add(element)
            
            k = len(nums_sorted) - 1
            j = i + 1

            while j < k:
                hi = nums_sorted[k]
                lo = nums_sorted[j]

                sum = hi + lo + element
                if sum == 0:
                
                    sublst = [element, lo, hi]
                    result.append(sublst)

                    j += 1
                    k -= 1

                    while j < k and nums_sorted[j] == nums_sorted[j - 1]:         
                        j += 1
                                          
                    while j < k and nums_sorted[k] == nums_sorted[k + 1]:
                        k -= 1
                
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
        return result
        