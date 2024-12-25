class Node:

    def __init__(self):
        self.children = {}
        self.is_end_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                current_node.children[c] = Node()
            
            current_node = current_node.children[c]
        current_node.is_end_word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            current_node = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in current_node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in current_node.children:
                        return False
                    current_node = current_node.children[c]
            return current_node.is_end_word
        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)