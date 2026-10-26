class Solution:
    def merge(self, L: List[int], R: List[int]) -> List[int]:
        i = 0
        j = 0
        sorted_array = []
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sorted_array.append(L[i])
                i += 1
            else:
                sorted_array.append(R[j])
                j += 1
        
        if i < len(L):
            sorted_array.extend(L[i : ])
        else:
            sorted_array.extend(R[j : ])
        
        return sorted_array


    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        m = n // 2
        L = self.sortArray(nums[ : m])
        R = self.sortArray(nums[m : ])
        return self.merge(L, R)
        