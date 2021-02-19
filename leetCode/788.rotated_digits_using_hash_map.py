class Solution:
    def rotatedDigits(self, N: int) -> int:
         # create a Hash Table for storing valid numbers
        numbers = {
            '0': '0',
            '1': '1',
            '2': '5',
            '5': '2',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        # initialize counter and set it to zero
        counter = 0
        
        # loop through numbers from one to N
        for e in range(1, N+1):
            temp = "" # initialize temp variable for storing rotated number
            for c in str(e): # loop through each character of number
                if c not in numbers: # if it's not present in our Hash Table simple break the loop
                    temp = str(e) # make temp variable equal to number itself
                    break # exit the loop
                else: # otherwise 
                    temp += numbers[c] # increment the temp variable            
            if temp != str(e): # if number after rotation is not equal to the number itself
                counter += 1 # increment counter
        return counter # return counter
