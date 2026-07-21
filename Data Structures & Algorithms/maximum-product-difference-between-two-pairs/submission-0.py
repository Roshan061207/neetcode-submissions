class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1=max2=0 #Getting things easier instead of jusing sort function
        min1=min2=float("infinity")
        for i in nums:
            if i > max2:
                if i>max1:
                    max1,max2=i,max1
                else:
                    max2=i
            if i<min2:
                if i < min1:
                    min1,min2=i,min1
                else:
                    min2=i
        return ((max1*max2)-(min1*min2))

                
