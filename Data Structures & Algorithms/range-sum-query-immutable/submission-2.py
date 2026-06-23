class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        totalsum=0
        for n in nums:
            totalsum+=n
            self.prefix.append(totalsum)
        

    def sumRange(self, left: int, right: int) -> int:
        rightsum=self.prefix[right]
        leftsum=self.prefix[left-1] if left>0 else 0
        return rightsum-leftsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)