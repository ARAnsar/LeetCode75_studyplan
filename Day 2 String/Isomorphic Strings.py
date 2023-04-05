class Solution(object):
    def isIsomorphic(self, s, t):
        check = {s[0]:t[0]}
        for i in range(0,len(s)):
            if t[i] in check.values():
                if s[i] in check:
                    if check[s[i]] != t[i]:
                        return False
                else:
                    return False
            else:
                if s[i] in check:
                    return False
                else:
                    check[s[i]] = t[i]
        return True
        