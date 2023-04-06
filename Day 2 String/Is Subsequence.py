class Solution(object):
    def isSubsequence(self, s, t):
        x = 0
        if 0 == len(s):
            return True
        for i in t:
            if i == s[x]:
                x = x + 1
                if x == len(s):
                    return True
        if x == len(s):
            return True
        else:
            return False