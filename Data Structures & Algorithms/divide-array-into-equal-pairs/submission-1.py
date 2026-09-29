class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen=set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                seen.remove(n)#If the pair is already is found rmeove it 

        return len(seen)==0
        