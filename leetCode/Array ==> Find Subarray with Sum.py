def find_subarray_with_sum(arr, target_sum):
    start = 0
    current_sum = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == target_sum:
            return arr[start:end + 1]

    return None  # No subarray found

# Example usage:
array = [1, 2, 3, 4, 5, 6, 7, 8]
target_sum = 15

result = find_subarray_with_sum(array, target_sum)

if result is not None:
    print(f"Subarray with sum {target_sum}: {result}")
else:
    print("No subarray found with the specified sum.")
