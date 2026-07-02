class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [strs]
        
        # Initialize a dictionary
        my_dict = {}

        for word in strs:
            lowered_word = word.lower()

            # Initialize a list for the alphabet
            my_list = [0] * 26

            for char in lowered_word:
                # Find the position of this character
                position = ord(char) - 97

                my_list[position] += 1
            
            # Convert the list into a tuple because the key of a dictionary
            # must be immutable
            my_tuple = tuple(my_list)

            if my_tuple in my_dict:
                my_dict[my_tuple].append(word)
            else:
                my_dict[my_tuple] = [word]
        
        return list(my_dict.values())

        