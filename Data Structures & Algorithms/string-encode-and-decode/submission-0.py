class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for st in strs:
                #add a delimiter
                result+=st+'|'
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        word = ''
        for c in s:
            if c == '|':
                #end of word. append it to result and reset the word
                result.append(word)
                word = ''
            else:
                word+=c
        return result

