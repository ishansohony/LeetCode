class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        
        def dfs(board, row, col, word):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            
            
            if board[row][col] != word[0]:
                return False
            
            if board[row][col] == word[0]:
                if len(word) == 1:
                    return True

                board[row][col] = "0"
                x = dfs(board, row + 1, col, word[1:]) or dfs(board, row, col + 1, word[1:]) or \
                dfs(board, row - 1, col, word[1:]) or dfs(board, row, col - 1, word[1:])
                board[row][col] = word[0]
            
            return x
            
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if (dfs(board, row, col, word)):
                        return True
                    
        return False
