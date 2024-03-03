class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        We initialize result as a list containing a single empty permutation [].

        We iterate over each integer num in nums.

        For each integer num, we generate new permutations by inserting num at every possible position in each permutation in result.

        We use a set seen to keep track of seen permutations. Before adding a new permutation to new_permutations, we check if it's already in seen. If not, we append it to new_permutations and add it to seen.

        After iterating over all integers in nums, result contains all unique permutations of nums, which we return.
        """
        result = [[]]
        for num in nums:
            new_permutations = []
            seen = set()
            for perm in result:
                for i in range(len(perm) + 1):
                    new_perm = perm[:i] + [num] + perm[i:]
                    if tuple(new_perm) not in seen:
                        new_permutations.append(new_perm)
                        seen.add(tuple(new_perm))
            result = new_permutations
        return result
