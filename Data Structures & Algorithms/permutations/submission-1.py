class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, used):
            if len(path) == len(nums):  # Base case: permutation complete
                result.append(path[:])  # Store a copy of path
                return

            for i in range(len(nums)):  # Try each number
                if used[i]:  # Skip already used numbers
                    continue
                
                used[i] = True  # Mark as used
                path.append(nums[i])  # Choose
                
                backtrack(path, used)  # Explore
                
                path.pop()  # Undo choice (backtrack)
                used[i] = False  # Unmark as used

        backtrack([], [False] * len(nums))  # Start recursion
        return result
     