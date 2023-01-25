def isPalindrome(self, x: int) -> bool:
    # int -> String
    x = str(x)
    return True if x[::-1] == x else False