class TrieNode():
    def __init__(self):
        self.map = {}
        self.end_of_word = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root

        for ch in word:
            if ch not in current.map:
                current.map[ch] = TrieNode()
            current = current.map[ch]
        current.end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root

        for ch in word:
            if ch not in current.map:
                return False
            current = current.map[ch]
        return current.end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root

        for p in prefix:
            if p not in current.map:
                return False
            current = current.map[p]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("door")
obj.insert("doer")
print(obj.search("dor"))
print(obj.startsWith("do"))
