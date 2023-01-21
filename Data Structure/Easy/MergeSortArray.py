def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	#appending the second list from the mth index
      nums1[m:] = nums2
      #sort the list to arrange them in non-decresing order
      nums1.sort()