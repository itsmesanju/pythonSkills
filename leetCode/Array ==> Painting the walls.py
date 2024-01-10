class Solution:
    """
    The paintWalls method uses dynamic programming to find the minimum cost of painting all walls 
    given the costs (cost) and time (time) associated with each wall. 
    
    Initialize an array money with float('inf') values, representing the minimum cost to paint the first i walls.
    Set money[0] to 0, indicating that the cost to paint 0 walls is 0.
    Iterate through the walls (i) and the possible number of walls painted (j) in reverse order.
    Update the money array based on the minimum cost to paint the current number of walls using the given cost and time information.
    Return the minimum cost to paint all walls (money[n]).
    """
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        money = [float('inf')]*(n+1)
        money[0]=0
        print(f"Money: {money}")
        for i in range(n):
            print(f"Paid: {i}")
            for j in range(n,0,-1):
                print(f"Free: {j}")
                money[j]=min(money[j],money[max(j-time[i]-1,0)]+cost[i])
                print(f"Money: {money}")

        return money[n]
