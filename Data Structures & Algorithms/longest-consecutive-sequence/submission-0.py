class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        given_numbers=set(nums)
        longestconsecutive=0
        for numbers in given_numbers:
            if (numbers-1)not in  given_numbers:
                length=0
                while(numbers+length) in given_numbers:
                    length+=1
                longestconsecutive=max(length,longestconsecutive)
        return longestconsecutive

        