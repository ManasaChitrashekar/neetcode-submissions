class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        subsetmap = {}
        res = []
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i]>stack[-1]:
                    stack.pop()
            if stack:
                subsetmap[nums2[i]]=stack[-1]
            else:
                subsetmap[nums2[i]]=-1
            stack.append(nums2[i])
        for num in nums1:
            res.append(subsetmap[num])
        return res