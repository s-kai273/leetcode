class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.child_dict = dict()

    def add_child(self, ch: str):
        self.child_dict[ch] = TrieNode(ch)

    def get_child(self, ch: str) -> "TrieNode | None":
        return self.child_dict.get(ch, None)

    def has_any_child(self) -> bool:
        return len(self.child_dict.keys()) > 0


class Trie:
    def __init__(self):
        self.root_node = TrieNode("0")

    def add(self, word: str):
        cur_node = self.root_node
        for ch in word:
            next_node = cur_node.get_child(ch)
            if not next_node:
                cur_node.add_child(ch)
                next_node = cur_node.get_child(ch)
            cur_node = next_node
        if not cur_node.get_child("0"):
            cur_node.add_child("0")

    def contains(self, prefix: str, with_end: bool = False):
        cur_node = self.root_node
        for ch in prefix:
            next_node = cur_node.get_child(ch)
            if not next_node:
                return False
            cur_node = next_node
        return cur_node.get_child("0") is not None if with_end else True


class PrefixTree:
    def __init__(self):
        self.word_trie = Trie()

    def insert(self, word: str) -> None:
        self.word_trie.add(word)

    def search(self, word: str) -> bool:
        return self.word_trie.contains(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self.word_trie.contains(prefix)
