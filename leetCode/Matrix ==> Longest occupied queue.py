def longest_queue_occupied(cinema):
    def count_consecutive_occupied(row):
        max_consecutive = 0
        consecutive = 0

        for seat in row:
            if seat == 1:
                consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)
            else:
                consecutive = 0

        return max_consecutive

    max_queue = 0

    # Check rows
    for row in cinema:
        max_queue = max(max_queue, count_consecutive_occupied(row))

    # Check columns
    for col in range(len(cinema[0])):
        column = [row[col] for row in cinema]
        max_queue = max(max_queue, count_consecutive_occupied(column))

    # Check diagonals
    for start_row in range(len(cinema)):
        diagonal = [cinema[i][start_row + i] for i in range(min(len(cinema) - start_row, len(cinema[0])))]
        max_queue = max(max_queue, count_consecutive_occupied(diagonal))

    for start_col in range(1, len(cinema[0])):
        diagonal = [cinema[start_col + i][i] for i in range(min(len(cinema[0]) - start_col, len(cinema)))]
        max_queue = max(max_queue, count_consecutive_occupied(diagonal))

    return max_queue

# Example usage:
cinema_layout = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
]

result = longest_queue_occupied(cinema_layout)
print(f"Longest queue occupied: {result}")
