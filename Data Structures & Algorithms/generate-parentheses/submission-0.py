class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def helper(i, curr, closed):

            print(curr)
            if i == n:
                while len(curr) < 2 * n:
                    curr += ")"

                res.append(curr)
                return
            
            # add a new parenthesis
            helper(i + 1, curr + "(", closed)



            # or close the current one
            if closed < i:
                helper(i, curr + ")", closed + 1)

        helper(0, "", 0)

        return res