class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # TC = O(2^2N) - 2 choices ^ height of the tree (2N)
        # SC = O(4^N* 2N) = 4^N number of strings with each of length 2N
        result,path = [],[]
        # we can generate all the combinations of the parenthesis and then prune the once
        # that are not valid
        def dfs(start, open_ct,close_ct):
            if start == 2*n:
                result.append("".join(path))
                return
            for p in "()":
                if p == "(" and open_ct <n:
                    path.append(p)
                    dfs(start+1,open_ct+1,close_ct)
                    path.pop()
                elif p == ")" and close_ct < open_ct:
                    path.append(p)
                    dfs(start+1,open_ct,close_ct+1)
                    path.pop()
        dfs(0,0,0)
        return result
        