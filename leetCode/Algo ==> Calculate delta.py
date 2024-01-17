def calculate_largest_delta(high_low_series):
    if len(high_low_series) < 2:
        return None  # Not enough data to calculate a delta

    largest_delta = float('-inf')

    for high, low in high_low_series:
        delta = high - low
        largest_delta = max(largest_delta, delta)

    return largest_delta

# Example usage:
daily_values = [
    (80, 60),  # High, Low for Day 1
    (90, 70),  # High, Low for Day 2
    (85, 65),  # High, Low for Day 3
    # Add more days as needed
]

result = calculate_largest_delta(daily_values)

if result is not None:
    print(f"Largest delta between any two days: {result}")
else:
    print("Insufficient data to calculate the delta.")
