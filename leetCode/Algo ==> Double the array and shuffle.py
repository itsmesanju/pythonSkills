import random

def double_and_shuffle(input_array):
    # Double the array
    doubled_array = input_array + input_array
    
    # Shuffle the doubled array
    random.shuffle(doubled_array)
    
    return doubled_array

# Example usage:
original_array = [1, 2, 3, 4, 5]
result_array = double_and_shuffle(original_array)

print("Original array:", original_array)
print("Doubled and shuffled array:", result_array)
