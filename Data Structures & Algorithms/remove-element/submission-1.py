class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0 #keeping the index 
        for i in range(len(nums)):
            if nums[i]!=val: #accessing the array name with mentioning its index and checking the condition is equal to the search value
                nums[k]=nums[i]
                k+=1
        return k
        