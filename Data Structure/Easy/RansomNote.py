def canConstruct(self, ransomNote, magazine):
    for char in ransomNote:
        if char in magazine:
            magazine = magazine.replace(char, "", 1) #if character is present in magazine remove it
        else:
            return False
    return True