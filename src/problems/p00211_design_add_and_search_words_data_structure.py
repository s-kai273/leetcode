class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.with_end = False

    def get_child(self, ch: str) -> "TrieNode | None":
        return self.children.get(ch, None)

    def add_child(self, ch: str):
        self.children[ch] = TrieNode(ch)

    def get_all_child(self) -> "List[TrieNode]":
        return self.children.values()


class WordDictionary:
    def __init__(self):
        self.root_node = TrieNode("0")

    def addWord(self, word: str) -> None:
        current = self.root_node
        for ch in word:
            next = current.get_child(ch)
            if not next:
                current.add_child(ch)
                next = current.get_child(ch)
            current = next
        current.with_end = True

    def _recursive(self, i: int, word: str, node: TrieNode):
        if i == len(word):
            return node.with_end
        ch = word[i]
        if ch == ".":
            for next in node.get_all_child():
                result = self._recursive(i + 1, word, next)
                if result:
                    return True
            return False
        next = node.get_child(ch)
        if not next:
            return False
        return self._recursive(i + 1, word, next)

    def search(self, word: str) -> bool:
        return self._recursive(0, word, self.root_node)
