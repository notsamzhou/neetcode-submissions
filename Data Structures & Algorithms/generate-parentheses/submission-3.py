class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def helper(i, curr, closed):

            if i == closed == n:

                res.append(curr)
                return
            
            # add a new parenthesis
            if i < n:
                helper(i + 1, curr + "(", closed)



            # or close the current one
            if closed < i:
                helper(i, curr + ")", closed + 1)

        helper(0, "", 0)

        return res