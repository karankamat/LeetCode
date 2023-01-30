def isAnagram(self, s, t):
    # unicode to string
    s = s.encode('ascii', 'ignore')
    t = t.encode('ascii', 'ignore')
    if "".join(sorted(s)) == "".join(sorted(t)):
        return True
    return False