class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for passenger in details:
            age1=passenger[11:13]
            age=int(age1)
            if age>60:
                count+=1
        return count

        