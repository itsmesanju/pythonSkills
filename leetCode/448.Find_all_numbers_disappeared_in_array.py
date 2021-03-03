
#Plain iterative.
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret=[]
        for items in range(1,len(nums)+1):
            if items not in nums:
                ret.append(items)
        return ret

#Use of set function to create a list.
#return the subtraction of original list and new set generated list

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = set(nums)
        if len(l) > 0:
            return list(set(range(1,len(nums)+1)) - l)
        else:
            return []
