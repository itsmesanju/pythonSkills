# Python3 implementation to find the
# Leftmost Column with atleast a
# 1 in a sorted binary matrix
import sys
N = 3
 
# Function to search for the
# leftmost column of the matrix
# with atleast a 1 in sorted
# binary matrix
def search(mat, n, m):
 
    a = sys.maxsize
     
    # Loop to iterate over all the
    # rows of the matrix
    for i in range (n):
        low = 0
        high = m - 1
        ans = sys.maxsize
         
        # Binary Search to find the
        # leftmost occurence of the 1
        while (low <= high):
            mid = (low + high) // 2
             
            # Condition if the column
            # contains the 1 at this
            # position of matrix
            if (mat[i][mid] == 1):
 
                if (mid == 0):
                    ans = 0
                    break
                 
                elif (mat[i][mid - 1] == 0):
                    ans = mid
                    break
                 
            if (mat[i][mid] == 1):
                high = mid - 1
            else:
                low = mid + 1
         
        # If there is a better solution
        # then update the answer
        if (ans < a):
            a = ans
    
    # Condition if the solution
    # doesn't exist in the matrix
    if (a == sys.maxsize):
        return -1
    return a + 1
 
# Driver Code
if __name__ == "__main__":
   
    mat = [[0, 0, 0],
           [1, 0, 1],
           [0, 1, 1]]
    print(search(mat, 3, 3))
   
