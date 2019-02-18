class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        alive = set()
        def update(board, row, col, alive):
            
            rowinc = colinc = rowdec = coldec = False
            cnt = 0
            if row + 1 < len(board): 
                rowinc = True
                cnt += board[row + 1][col] 
            if col + 1 < len(board[0]): 
                colinc = True
                cnt += board[row][col + 1]
            if row - 1 >= 0: 
                rowdec = True
                cnt += board[row - 1][col]    
            if col - 1 >= 0: 
                coldec = True
                cnt += board[row][col - 1]
            if rowdec and coldec:
                cnt += board[row - 1][col - 1]
            if rowdec and colinc:
                cnt += board[row - 1][col + 1]
            if rowinc and coldec:
                cnt += board[row + 1][col - 1]
            if rowinc and colinc:
                cnt += board[row + 1][col + 1]
                
            if(board[row][col] == 1):
                if cnt == 2 or cnt == 3:
                    alive.add((row,col))
            
            else:
                if cnt == 3:
                    alive.add((row,col))
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                update(board, row, col, alive)
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) in alive:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
                    
        
        
                    
