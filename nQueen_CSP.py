class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n  
        self.remaining_values = [set(range(n)) for _ in range(n)]  

    def place_queen(self, col, row): 
        self.board[col] = row
        for c in range(self.n):
            if c != col:
                if row in self.remaining_values[c]:
                    self.remaining_values[c].remove(row)
                distance = col - c
                if row + distance in self.remaining_values[c]:
                    self.remaining_values[c].remove(row + distance)
                if row - distance in self.remaining_values[c]:
                    self.remaining_values[c].remove(row - distance)

    def remove_queen(self, col):
        row = self.board[col]
        self.board[col] = -1  
        for c in range(self.n):
            if c != col:
                self.remaining_values[c].add(row)               
                distance = col - c
                if row + distance < self.n:
                    self.remaining_values[c].add(row + distance)
                if row - distance >= 0:
                    self.remaining_values[c].add(row - distance)

    def select_unassigned_variable(self):
        min_remaining_values = float('inf')
        min_col = -1
        for c in range(self.n):
            if self.board[c] == -1: 
                remaining_count = len(self.remaining_values[c])
                if remaining_count < min_remaining_values:
                    min_remaining_values = remaining_count
                    min_col = c
        return min_col

    def is_complete(self):
        return all(row != -1 for row in self.board)

    def backtrack_search(self):
        if self.is_complete():
            return True  
        col = self.select_unassigned_variable()  
        remaining_rows = list(self.remaining_values[col])  
        for row in remaining_rows:  
            self.place_queen(col, row)  
            if self.backtrack_search():  
                return True  
            self.remove_queen(col)  
        return False 

    def solve(self):
        if self.backtrack_search():
            return self.board  
        else:
            return None  

def create_board(n, queens_positions):
    """Creates an n x n board with queens placed according to queens_positions."""
    board = [["." for _ in range(n)] for _ in range(n)]
    for col in range(n):
        board[queens_positions[col]][col] = "Q"
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


n = 8

n_queens = NQueens(n)
solution = n_queens.solve()
if solution:
    board = create_board(n, solution)
    print("Solution found:")
    print_board(board)
else:
    print("No solution exists.")