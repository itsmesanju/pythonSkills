'''Runtime complexity: Linear,
O(n)

Memory Complexity: Linear,
O(n)

This problem can be solved in a simple linear scan algorithm. We know that input is sorted by starting timestamps. Here is the approach we are following:

List of input intervals is given, and we’ll keep merged intervals in the output list.
For each interval in the input list:
If the input interval is overlapping with the last interval in the output list then we’ll merge these two intervals and update the last interval of the output list with the merged interval.
Otherwise, we’ll add an input interval to the output list.
'''

class Pair:

  def __init__(self, first, second):
    self.first = first
    self.second = second

def merge_intervals(v):
  if v == None or len(v) == 0 :
    return None

  result = []
  result.append(Pair(v[0].first, v[0].second))

  for i in range(1, len(v)):
    x1 = v[i].first
    y1 = v[i].second
    x2 = result[len(result) - 1].first
    y2 = result[len(result) - 1].second

    if y2 >= x1:
      result[len(result) - 1].second = max(y1, y2)
    else:
      result.append(Pair(x1, y1))

  return result;

v = [Pair(1, 5), Pair(3, 1), Pair(4, 6), 
     Pair(6, 8), Pair(10, 12), Pair(11, 15)]

result = merge_intervals(v)

for i in range(len(result)):
  print("[" + str(result[i].first) + ", " + str(result[i].second) + "]", end =" ")
