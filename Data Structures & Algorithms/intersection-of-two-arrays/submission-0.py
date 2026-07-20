class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited=set(nums1)
        res=[]
        for i in nums2:
            if i in visited:
                res.append(i)
                visited.remove(i)
        return res
        