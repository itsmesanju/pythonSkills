class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        suggestions = []
        self._collect_suggestions(node, prefix, suggestions)
        return suggestions

    def _collect_suggestions(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)

        for char, child_node in node.children.items():
            self._collect_suggestions(child_node, prefix + char, suggestions)

# Example usage:
autocomplete_trie = Trie()
words = ["apple", "app", "application", "banana", "bat"]
for word in words:
    autocomplete_trie.insert(word)

prefix = "app"
if autocomplete_trie.search(prefix):
    suggestions = autocomplete_trie.autocomplete(prefix)
    print(f"Autocomplete suggestions for '{prefix}': {suggestions}")
else:
    print(f"No suggestions found for '{prefix}'")
