class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        letters2 = {}
        for i in t:
            if i in letters2:
                letters2[i] += 1
            else:
                letters2[i] = 1
        if letters == letters2:
            return True
        return False
            
        