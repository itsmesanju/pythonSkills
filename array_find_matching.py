array_in=[1,2,3,5,61,9,10,22]
total = 16
size=len(array_in)

for i in range(size):
    for j in range(i+1, size, 1):
        if array_in[i] + array_in[j] == total:
            print(f'Possible solution is with {array_in[i]} @ index: {i}, {array_in[j]} @ index: {j}')

