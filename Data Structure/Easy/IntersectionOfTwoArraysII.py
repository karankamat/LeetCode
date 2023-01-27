from collections import Counter
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    num_counter = Counter(nums1)
    for i in nums2:
        if i in num_counter:
            if num_counter[i]>0:
                result.append(i)
            num_counter[i] -= 1
    return result