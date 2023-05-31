class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vows = 0
        n = len(s)
        i = 0
        j = 0
        c = 0
        while j<n:
            if j-i<k:
                if s[j] in vowels:
                    c+=1
                j+=1
            else:
                if s[i] in vowels:
                    c-=1
                i+=1
            vows = max(vows, c)
        return vows