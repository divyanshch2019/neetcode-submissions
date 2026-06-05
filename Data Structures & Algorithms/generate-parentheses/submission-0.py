class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
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
        