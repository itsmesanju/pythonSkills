'''Runtime complexity: Linear, 
O(n)

Memory Complexity: Constant, 
O(1)

The values in the array represent the cost of a stock each day. As we can buy and sell the stock only once, we need to find the best buy and sell prices for which our profit is maximized (or loss is minimized) over a given span of time.

There is a tricky linear solution to this problem that requires maintaining current_buy_price (which is the smallest number seen so far), current_profit, and global_profit as we iterate through the entire array of stock prices.

At each iteration, we will compare the current_profit with the global_profit and update the global_profit accordingly.
'''

import sys
def find_buy_sell_stock_prices(array):
  if array == None or len(array) < 2:
    return None

  current_buy = array[0]
  global_sell = array[1]
  global_profit = global_sell - current_buy

  current_profit = -sys.maxsize - 1

  for i in range(1, len(array)):
    current_profit = array[i] - current_buy

    if current_profit > global_profit:
      global_profit = current_profit
      global_sell = array[i]

    if current_buy > array[i]:
      current_buy = array[i];

  result = global_sell - global_profit, global_sell                 
   
  return result

array = [1, 2, 6, 4, 3, 2, 1, 2, 5]  
result = find_buy_sell_stock_prices(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))

array = [10, 6,5, 3, 2, 1]
result = find_buy_sell_stock_prices(array)
print("Buy Price: " + str(result[0]) + ", Sell Price: " + str(result[1]))
