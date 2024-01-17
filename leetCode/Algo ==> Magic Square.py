def generate_odd_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]

    row, col = 0, n // 2
    num = 1

    while num <= n**2:
        magic_square[row][col] = num
        num += 1

        new_row, new_col = (row - 1) % n, (col + 1) % n

        if magic_square[new_row][new_col] == 0:
            row, col = new_row, new_col
        else:
            row = (row + 1) % n

    return magic_square

# Example usage:
n = 3
magic_square = generate_odd_magic_square(n)
for row in magic_square:
    print(row)
