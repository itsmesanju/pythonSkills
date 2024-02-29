class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        we dont need actual indices, we dont care about sequence or order so we don't need sort.

        Just count number of elements which are less than or equal to given target. say lessThanOrEqualCount
        Then count number of elements which are strictly less than given target onlyLessThanCount

        if lessThanOrEqualCount = onlyLessThanCount: return empty
        or else all numbers between them
        """

        lessThanEqual = 0
        onlyLess = 0
        for i in nums:
            if i <= target:
                lessThanEqual += 1
            if i < target:
                onlyLess += 1

        return list(range(onlyLess, lessThanEqual))

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
                
        return result

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = [x for x in range(len(nums))]
        sorting_nums = sorted(nums)
        dictionary = dict(zip(indices, sorting_nums))
        answer = [key for key, value in dictionary.items()
        if value==target]
        return answer
        

