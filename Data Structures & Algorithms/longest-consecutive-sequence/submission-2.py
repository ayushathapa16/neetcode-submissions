class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_sorted = sorted(nums)

        seq_counts = []
        count_so_far = 1
        for i in range(0, len(nums) - 1):
            # If there are repeated elements, move onto the next one
            if nums_sorted[i] == nums_sorted[i + 1]:
                continue
            
            if nums_sorted[i] + 1 == nums_sorted[i + 1]:
                count_so_far += 1
            else:
                seq_counts.append(count_so_far)
                count_so_far = 1
        seq_counts.append(count_so_far)
        return max(seq_counts)

        