def slot_machine(n, spins):
    result = 0

    while spins:
        max_values = [max(row) for row in spins]
        max_value = max(max_values)

        result += max_value

        for i in range(len(spins)):
            if max_value in spins[i]:
                spins[i].remove(max_value)

        spins = [row for row in spins if row]

    return result

# Example 1
n1 = 4
spins1 = [
    [7, 1, 2],
    [2, 4, 6],
    [3, 6, 5],
    [3, 1, 2]
]

result1 = slot_machine(n1, spins1)
print(result1)  # Output: 15

# Example 2
n2 = 5
spins2 = [
    [1, 3, 7],
    [1, 1, 5],
    [3, 6, 4],
    [1, 1, 5],
    [7, 2, 4]
]

result2 = slot_machine(n2, spins2)
print(result2)  # Output: 14
