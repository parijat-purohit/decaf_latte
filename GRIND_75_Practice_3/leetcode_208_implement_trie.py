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
        curr = self.root

        for ch in word:
            if ch not in curr.map:
                curr.map[ch] = TrieNode()
            curr = curr.map[ch]
        curr.end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for ch in word:
            if ch not in curr.map:
                return False
            curr = curr.map[ch]
        return curr.end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr.map:
                return False
            curr = curr.map[ch]
        return True


t1 = Trie()
t1.insert('artichoke')
print(t1.search('art'))
print(t1.startsWith('art'))
