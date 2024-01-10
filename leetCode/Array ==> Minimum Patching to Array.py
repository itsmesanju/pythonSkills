class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered = 1 #Smallest integer to start with
        patch = 0
        index = 0
        print(f" Input Array: {nums}")
        
        while covered <= n: #Run until covered is less than n to test
            if index < len(nums) and nums[index] <= covered: #If coverage is larger than the array item
                covered = covered + nums[index]
                index = index + 1
            else:
                covered = covered * 2 # Double the current covered range by adding a patch number.
                patch = patch + 1
        return patch      
