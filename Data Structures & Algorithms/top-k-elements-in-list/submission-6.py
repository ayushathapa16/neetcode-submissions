class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Create a mapping between elements and their frequencies
        element_to_count = {}
        for i in nums:
            if i in element_to_count:
                element_to_count[i] += 1
            else:
                element_to_count[i] = 1

        # Step 2: Initialize a frequency list
        freq_list = [[] for i in range(0, len(nums) + 1)]

        # Step 3: Fill in the frequency list
        for key, value in element_to_count.items():
            freq_list[value].append(key)
        
        top_k = []
        for i in range(len(nums), -1, -1):
            lst = freq_list[i]

            if len(lst) > 0:
                top_k.extend(lst)

            if len(top_k) >= k:
                return top_k[:k + 1]





        