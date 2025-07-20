class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res=[]
        def backtrack(index, curStr):
            if index==len(digits):
                res.append(curStr)
                return
            
            for c in phoneMap[digits[index]]:
                backtrack(index+1, curStr+c)
        backtrack(0,"")

        return res
        