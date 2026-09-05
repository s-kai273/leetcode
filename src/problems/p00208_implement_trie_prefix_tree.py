class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.child_dict = dict()

    def add_child(self, ch: str):
        self.child_dict[ch] = TrieNode(ch)

    def get_child(self, ch: str) -> "TrieNode | None":
        return self.child_dict.get(ch, None)


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

    def contains(self, prefix: str):
        cur_node = self.root_node
        for ch in prefix:
            next_node = cur_node.get_child(ch)
            if not next_node:
                return False
            cur_node = next_node
        return True


class PrefixTree:
    def __init__(self):
        self.word_set = set()
        self.word_trie = Trie()

    def insert(self, word: str) -> None:
        self.word_set.add(word)
        self.word_trie.add(word)

    def search(self, word: str) -> bool:
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        return self.word_trie.contains(prefix)
