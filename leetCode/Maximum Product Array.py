#Brute force methid
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        """
        Initialize ans, maxi, and mini to the first element of the nums array.
        Iterate through the elements of the nums array from the second element to the end.
        Within each iteration:
                Check if the current element is negative. If it is, swap the values of maxi and mini. This is because multiplying a negative number with the current maxi can result in a larger product.
                Update maxi to be the maximum of the current element and the product of the current maxi and the current element.
                Update mini to be the minimum of the current element and the product of the current mini and the current element.
                Update ans with the maximum of the current ans and maxi.
        After the loop, ans will hold the maximum product of a subarray.
        """
        ans, maxi,mini = nums[0],nums[0],nums[0]

        for i in range(1,len(nums)):
            if nums[i] < 0:
                maxi,mini=mini,maxi
            maxi = max(nums[i],maxi*nums[i])
            mini = min(nums[i],mini*nums[i])
            ans = max(ans,maxi)
        return ans
