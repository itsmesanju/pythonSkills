import heapq

def min_cost_to_connect_sticks(sticks):
    # Convert the list of sticks into a min-heap.
    # Use heapq as priority queue so that smallest size sticks are picked.
    # Insert the joined stick back in the array and repeat the operation
  
    heapq.heapify(sticks)
    
    total_cost = 0

    while len(sticks) > 1:
        # Extract the two smallest sticks
        x = heapq.heappop(sticks)
        y = heapq.heappop(sticks)

        # Connect the sticks and add the cost
        cost = x + y
        total_cost += cost

        # Put the connected stick back into the heap
        heapq.heappush(sticks, cost)

    return total_cost

# Example usage:
sticks = [5, 2, 8, 1]
result = min_cost_to_connect_sticks(sticks)
print(f"The minimum cost to connect all sticks is: {result}")
