'''Implementation of the Trie data structure as described in https://www.youtube.com/watch?v=AXjmTQ8LEoI.
'''
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, s):
        current = self
        for c in s:
            node = current.children.get(c)
            if node is None:
                node = current.children[c] = TrieNode()
            current = node
        current.is_end_of_word = True

    def search(self, s, whole_word=False):
        current = self
        for c in s:
            node = current.children.get(c)
            if node is None:
                return False
            current = node
        if whole_word:
            return current.is_end_of_word
        else:
            return True

    def delete(self, s):
        return self.__delete(s, 0)

    def __delete(self, s, index=0):
        if index >= len(s):
            return
        c = s[index]
        node = self.children.get(c)
        if node is None:
            return
        if index == (len(s) - 1) and node.is_end_of_word:
            node.is_end_of_word = False
        else:
            node.__delete(s, index+1)
        if not node:
            self.children.pop(c)

    def __bool__(self):
        '''Check if the node is empty and can be safely deleted.'''
        return bool(self.children) or self.is_end_of_word


def test_can_be_searched_after_insertion():
    root = TrieNode()
    root.insert("satoru")
    root.insert("satori")
    root.insert("dodoro")
    assert root.search("s")
    assert not root.search("e")
    assert root.search("sat")
    assert not root.search("sat", whole_word=True)
    assert root.search("satori", whole_word=True)
    assert root.search("dodoro", whole_word=True)


def test_can_be_deleted_after_insertion():
    root = TrieNode()
    root.insert("satoru")
    root.insert("satori")
    root.insert("dodoro")
    root.insert("apple")
    root.insert("ape")
    root.delete("satoru")
    assert not root.search("satoru")
    root.delete("ape")
    assert not root.search("ape")
    assert root.search("apple")
