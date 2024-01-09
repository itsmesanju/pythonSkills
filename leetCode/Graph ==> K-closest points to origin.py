class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        """
        Store all distances and their corresponding points in a hash table.

        Then sort the dictionary keys from max to min in a list, and iterate through
        distances from min to max until the list answer is superior to k elements long.

        Then, return the k first elements from the answer list, in case there are more points than need to be in there.
        """
        # Store distances and points that fit in hash table
        distances = {}

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)

            if distance in distances:
                distances[distance].append([x, y])
            else:
                distances[distance] = [[x, y]]
        
        print(distances)
        # Sort all distances from max to min
        sorted_distances = list(distances.keys())
        sorted_distances.sort(reverse=True)

        # Now iterate through points with min to max distance
        # until all k min points have been found
        answer = []

        while len(answer) < k:
            tmp_distance = sorted_distances.pop()
            answer += distances[tmp_distance]

        return answer
