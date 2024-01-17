class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        A Trie data structure (data) is used to store the words efficiently.
        The findWords method iterates through the list of words and constructs a Trie for quick lookup.
        The helper function is a recursive depth-first search (DFS) function that traverses the board to find words. It updates the result list (res) when a word is found and marks the visited cells with *.
        The main loop iterates through each cell in the board and calls the helper function to explore possible words starting from that cell.
        """
        res = []
        data = {}


        for word in words:
            root = data
            for char in word:
                if char not in root:
                    root[char] = {}
                root = root[char]  
            root["#"] = word
        print(root)
        print(data)

        def helper(r, c, node, curr):  
            if r >= len(board) or c>=len(board[0]) \
               or r < 0 or c < 0 \
               or board[r][c] == "*":
                return

            val = board[r][c]

            if val not in node:
                return
            
            curr+=val
            node = node[val]
            if "#" in node and node["#"]:
                res.append(node["#"])
                node["#"] = ""
            
            board[r][c] = "*" #visited
            helper(r+1,c,node,curr)
            helper(r-1, c,node,curr)
            helper(r,c+1,node, curr )
            helper(r,c-1, node, curr)
            board[r][c] = val
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                helper(r, c, data, "") 
          
        return res
