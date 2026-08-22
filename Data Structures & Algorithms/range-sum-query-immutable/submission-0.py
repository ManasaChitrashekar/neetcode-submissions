class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        prefixsum = 0 
        for n in nums:
            prefixsum +=n
            self.prefix.append(prefixsum)


    def sumRange(self, left: int, right: int) -> int:
        l = self.prefix[left-1] if left > 0 else 0
        return self.prefix[right]-l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)