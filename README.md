# N-Queens Problem Solver by Constraint Satisfaction (CSP)

This project implements a solution to the N-Queens problem using a Constraint Satisfaction Problem (CSP) approach. The N-Queens problem involves placing N chess queens on an N×N chessboard so that no two queens threaten each other.

## Problem Description

The goal is to place N queens on a chessboard such that no two queens share the same row, column, or diagonal. This is a classic problem in computer science and is often used to illustrate backtracking algorithms.

## Implementation

### Classes and Functions

- **NQueens**: This class encapsulates the N-Queens solver with the following methods:
  - `__init__(self, n)`: Initializes the N-Queens problem for an n x n board.
  - `place_queen(self, col, row)`: Places a queen at the specified column and row, updating the board and remaining values.
  - `remove_queen(self, col)`: Removes a queen from the specified column and updates the board and remaining values.
  - `select_unassigned_variable(self)`: Selects the next unassigned column based on the Minimum Remaining Values (MRV) heuristic.
  - `is_complete(self)`: Checks if all queens have been placed.
  - `backtrack_search(self)`: Recursively searches for a valid placement of queens using backtracking.
  - `solve(self)`: Initiates the backtracking search and returns the solution if found.

- **create_board(n, queens_positions)**: This function creates an n x n chessboard with queens placed according to the provided queen positions.

- **print_board(board)**: This function prints the board, displaying queens as "Q" and empty squares as ".".

# Output
The program will print the solution for the N-Queens problem, displaying the board with queens represented by "Q". If no solution exists, it will indicate that as well.

# Example Output
Solution found:
. Q . . . . . .
. . . . Q . . .
Q . . . . . . .
. . . . . . Q .
. . . . . Q . .
. . Q . . . . .
. . . . . . . Q
. . . Q . . . .

### Instructions to Use This README

1. Replace `yourusername` in the cloning URL with your actual GitHub username.
2. Save this content in a file named `README.md` in your project directory.
3. Modify any sections further as needed to fit your project specifics.

Feel free to ask if you need additional modifications or more sections!

