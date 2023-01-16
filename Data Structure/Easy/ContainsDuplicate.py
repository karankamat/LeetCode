class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
	  # empty dictionary
        freq_count = dict()
        for element in nums:
		# if a key is present for the element it will return True as the element is being repeated
            if element in freq_count.keys():
                return True
		# if not present the key for the element will be generate and value 1 will be assigned
            else:
                freq_count[element] = 1

        return False     