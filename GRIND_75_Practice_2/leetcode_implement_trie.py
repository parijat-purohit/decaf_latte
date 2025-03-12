class TrieNode():
    def __init__(self):
        self.children = {}
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
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]

        return current.end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
