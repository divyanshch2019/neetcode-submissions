class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in ("+","-","*","/"):
                #pop 2 elements from the stack and apply the operation
                #push the result back
                if len(st)>=2:
                    second_operand = st.pop()
                    first_operand = st.pop()
                    result = 0
                    if t =="+":
                        result = first_operand+second_operand
                    elif t =="-":
                        result = first_operand-second_operand
                    elif t == "*":
                        result = first_operand*second_operand
                    else:
                            result = int(first_operand/second_operand)
                            
                    st.append(result)
            else:
                st.append(int(t))
        return st.pop()

        