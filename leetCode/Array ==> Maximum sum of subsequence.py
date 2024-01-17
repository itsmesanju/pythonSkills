def max_sum_k_elements(arr, k):
    n = len(arr)

    if k >= n:
        return sum(arr)

    max_sum = 0

    for _ in range(k):
        if arr[0] > arr[-1]:
            max_sum += arr.pop(0)
        else:
            max_sum += arr.pop()

    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
result = max_sum_k_elements(arr, k)
print(f"The maximum sum of {k} elements is: {result}")
