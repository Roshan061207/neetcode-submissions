class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word =s.split()
        if len(pattern)!=len(word):
            return False
        Pattern2s,s2Pattern={},{}
        for i in range(len(pattern)):
            c1,c2=pattern[i],word[i]
            if ((c1 in Pattern2s and Pattern2s[c1]!=c2)or(c2 in s2Pattern and s2Pattern[c2]!=c1)):
                return False
            Pattern2s[c1]=c2
            s2Pattern[c2]=c1
        return True
        