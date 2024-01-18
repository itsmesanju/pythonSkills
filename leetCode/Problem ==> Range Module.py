class RangeModule:
    """
    This code defines a class RangeModule to manage ranges and perform operations such as adding, querying, and removing ranges. 
    The implementation uses a list (self.ans) to store the intervals.
    """

    def __init__(self):
        self.ans = []

    def addRange(self, left, right):
        """
        Uses binary search (bisect_left and bisect_right) to find the appropriate positions to insert or update intervals.
        Modifies the list self.ans by inserting or updating intervals based on the given left and right values.
        """
        i = bisect.bisect_left(self.ans,left)
        j = bisect.bisect_right(self.ans,right)
        self.ans[i:j] = [left]*(i%2==0) + [right]*(j%2==0)

    def queryRange(self, left, right):
        """
        Uses binary search to find the positions where left and right should be inserted in the list.
        Checks if the positions are equal and if the count of intervals between them is odd. 
        
        Returns True if so, indicating that the queried range is covered.
        """
        i = bisect.bisect_right(self.ans,left)
        j = bisect.bisect_left(self.ans,right)

        return i == j and i%2 == 1

    def removeRange(self, left, right):
        """
        Uses binary search to find the positions to insert or update intervals.
        Modifies the list self.ans by inserting or updating intervals based on the given left and right values. 
        The modification ensures that the specified range is removed.
        """
        i = bisect.bisect_left(self.ans,left)
        j = bisect.bisect_right(self.ans,right)
        self.ans[i:j] = [left]*(i%2==1) + [right]*(j%2==1)

        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
