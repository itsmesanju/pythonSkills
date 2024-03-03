class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        backtrack function: This function recursively explores all possible combinations starting from the start index. It adds each candidate to the current path and continues exploring with the updated target and path. If the target becomes zero, it means a valid combination is found, so it adds the current path to the result. If the target becomes negative or if we've exhausted all candidates, the function returns without making any changes.

The main function sorts the candidates list to handle duplicates efficiently. It then calls the backtrack function with the starting index as 0, the target, and an empty path.
        """
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  # Skip duplicates
                if candidates[i] > target:
                    break  # No need to continue if the candidate is greater than target
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
        
        result = []
        candidates.sort()  # Sort candidates to handle duplicates
        backtrack(0, target, [])
        return result
