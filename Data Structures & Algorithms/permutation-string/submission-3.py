class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Step 1: Build a hashmap of characters and their counts of s1 and create the first window for s2
        s1_count = {}
        s2_count = {}
        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
        if s1_count == s2_count:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            # Remove current l from hashmap and move it forward
            if s2_count[s2[l]] == 1:
                s2_count.pop(s2[l])
            else:
                s2_count[s2[l]] -= 1
            l += 1

            # Add r character to hashmap and check whether we have found s1
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1

            if s1_count == s2_count:
                return True
        
        return False