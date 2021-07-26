'''Runtime complexity: Linear,
O(n)

Memory Complexity: Constant,
O(1)

Keep two markers: read_index and write_index and point them to the end of the array. Let’s take a look at an overview of the algorithm.

While moving read_index towards the start of the array:

If read_index points to 0, skip.
If read_index points to a non-zero value, write the value at read_index to write_index and decrement write_index.
Assign zeros to all the values before the write_index and to the current position of write_index as well.

'''
def move_zeros_to_left(A):
  if len(A) < 1:
    return

  lengthA = len(A)
  write_index = lengthA - 1
  read_index = lengthA - 1

  while(read_index >= 0):
    if A[read_index] != 0:
      A[write_index] = A[read_index]
      write_index -= 1

    read_index -= 1

  while(write_index >= 0):
    A[write_index]=0;
    write_index-=1
    
v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print("Original Array:", v)

move_zeros_to_left(v)

print("After Moving Zeroes to Left: ", v)
