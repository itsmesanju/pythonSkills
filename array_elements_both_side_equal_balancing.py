#Find the index of an element in a list such that sum of elements to the left of the index is equal to sum of elements to the right of the index
# Input : 6 4 5 10
# Output : 2


def checkFunction(arr, size) : 
  
    right_sum, left_sum = 0, 0
  
    for i in range(1, size) : 
        right_sum += arr[i] 
  
    i, j = 0, 1
  
    while j < size : 
        right_sum -= arr[j] 
        left_sum += arr[i] 
  
        if left_sum == right_sum : 
            return i + 1 
  
        j += 1
        i += 1
  
    return "Not Found"
  

if __name__ == "__main__":
    array_input = [6,4,5,10]
    size=len(array_input)
    print(checkFunction(array_input,size))
