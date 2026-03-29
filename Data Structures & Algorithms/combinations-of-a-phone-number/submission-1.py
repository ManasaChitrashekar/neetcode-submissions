class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res= []
        digToChar = {
             "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i,op):
            if(len(op)==len(digits)):
                res.append(op)
                return 

            for c in digToChar[digits[i]]:
                dfs(i+1,op+c)

        if digits:
            dfs(0,"")
        return res            