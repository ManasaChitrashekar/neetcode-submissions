class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reslist = []
        res = (digits[-1]+1)
        carry = res //10 
        res = res % 10
        print(carry)
        reslist.insert(0,res)
        for i in range(len(digits)-2,-1,-1):
            res = (carry + digits[i])
            carry = res //10 
            res = res %10 
            reslist.insert(0,res)
        if carry !=0:
            reslist.insert(0,carry)
        return reslist 