class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        To explain the idea of the algorithm, I want to give you an example and go with you through it. Let's get started!

Let's imagine that num1 = 12 and num2 = 34. Now let's break down the multiplication process into separated steps:
12 * 34 = (10 + 2) * (30 + 4) = (10 * 30 + 10 * 4) + (2 * 30 + 2 * 4) =
= ((1 * 3) * 10 + (1 * 4)) * 10 + ((2 * 3) * 10 + (2 * 4)) =
= 340 + 68 = 408


        """
        totol = 0
        for n1 in num1:
            #print(f"N1: {n1}")

            totol *= 10
            product = 0
            for n2 in num2:
                #print(f"N2: {n2}")

                product = product * 10 + int(n1) * int(n2)
                #print(f"product: {product}")
            totol += product
            print(f"Total: {totol}")
        
        return str(totol)        
