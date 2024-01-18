class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @lru_cache(None)
        def helper(start, max_piles): 
            #start:  current index in the list of piles.
            #max_piles: maximum number of consecutive piles the current player can take.
            print(start, max_piles)


            total = 0 
            if start >= len(piles): 
                return 0 
            
            #Calculating the Total:
            """
            no_of_pile: the number of piles the current player can take in this turn
            The function iterates over possible values of X () in the range from 1 to 2 * max_piles.

            For each no_of_pile, it calculates the total number of stones the current player can collect in this turn. 
            
            This is done by taking the sum of the remaining piles (sum(piles[start:])) and subtracting the recursively calculated value for the opponent's turn (helper(start+X, max(M, X))).
            """

            for no_of_pile in range(1, 2 * max_piles + 1): 
                total = max(total, sum(piles[start:]) - helper(start+no_of_pile, max(max_piles, no_of_pile)))
            return total 


        return helper(0, 1)
