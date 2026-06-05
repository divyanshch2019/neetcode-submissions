class Solution:
    def isValid(self, s: str) -> bool:
        #we can stack LIFO property to check the validity of the strings
        st = []
        open_paren = {'(','{','['}
        for paren in s:
            if paren in open_paren:
                st.append(paren)
                continue
            if st:
                if paren == ')' and st[-1]!='(': return False
                if paren == '}' and st[-1]!='{': return False
                if paren == ']' and st[-1]!='[': return False
                st.pop()
                continue
            return False
        return len(st)==0

        