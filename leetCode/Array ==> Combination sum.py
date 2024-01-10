class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        """In this solution, the result list is a list of lists, where result[i] contains all unique combinations 
        that sum up to i. The outer loop iterates through each candidate, the middle loop iterates through the target values,   
        and the inner loop iterates through the combinations for the current target value.
        """
        result = [[] for _ in range(target + 1)]
        result[0].append([])
        
        for candidate in candidates:
            for i in range(candidate, target + 1):
                for combination in result[i - candidate]:
                    result[i].append(combination + [candidate])
        return result[target]
