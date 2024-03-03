class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        We initialize result as a list containing a single empty permutation [].

        We iterate over each integer num in nums.

        For each integer num, we generate new permutations by inserting num at every possible position in each permutation in result.

        We update result to contain the newly generated permutations.

        After iterating over all integers in nums, result contains all permutations of nums, which we return.
        """
        result = [[]]
        for num in nums:
            new_permutations = []
            for perm in result:
                for i in range(len(perm) + 1):
                    new_permutations.append(perm[:i] + [num] + perm[i:])
            result = new_permutations
        return result
