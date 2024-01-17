import random

def generate_bingo_board():
    # Define the ranges for each column (B: 1-15, I: 16-30, N: 31-45, G: 46-60, O: 61-75)
    column_ranges = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]

    # Initialize an empty 5x5 Bingo board
    bingo_board = [["" for _ in range(5)] for _ in range(5)]

    # Fill in the numbers for each column
    for col in range(5):
        start, end = column_ranges[col]
        column_numbers = random.sample(range(start, end + 1), 5)

        # Replace the central square with "FREE"
        if col == 2:
            column_numbers[2] = "FREE"

        # Assign numbers to the board
        for row in range(5):
            bingo_board[row][col] = column_numbers[row]

    return bingo_board

# Example usage:
bingo_board = generate_bingo_board()

# Print the Bingo board
for row in bingo_board:
    print(row)
