class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        

    def insert(self, word: str) -> None:
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = PrefixTree()
            node = node.children[w]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self
        for w in word:
            if w not in node.children: return False
            node = node.children[w]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for w in prefix:
            if w not in node.children: return False
            node = node.children[w]
        return node is not None
        
        