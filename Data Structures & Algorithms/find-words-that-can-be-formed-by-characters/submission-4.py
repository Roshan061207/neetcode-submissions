class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=Counter(chars)
        res=0
        for w in words:
            currentword=defaultdict(int)
            good=True
            for c in w:
                currentword[c]+=1
                if c not in count or currentword[c]>count[c]:
                    good=False
                    break
            if good:
                res+=len(w)
        return res

        