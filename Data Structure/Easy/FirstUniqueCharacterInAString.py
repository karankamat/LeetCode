def firstUniqChar(self, s: str) -> int:
    sset = set(s) # set of all the characters of the string
    scounter = Counter(s) # occurance count of each character
    # creating a list of elements indices whose occurance is less than 1
    index_list = [s.index(char) for char in list(sset) if scounter[char] < 2]
    if not index_list:
        return -1 # no unique character
    return min(index_list)