class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        brackets = [""] * (n * 2)
        result = []
        
        def solve(ind, total, brackets, result):
            if ind >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return
            
            if total > len(brackets) // 2:
                return
                
            if total < 0:
                return
            
            brackets[ind] = "("
            sum_val = total + 1
            solve(ind + 1, sum_val, brackets, result)
            
            brackets[ind] = ")"
            sum_val = total - 1
            solve(ind + 1, sum_val, brackets, result)

        solve(0, 0, brackets, result)
        return result