""" 
given an integer array nums, return true if 
any value appears at least twine in the array,
and return false if every element in distinct



a BigO(n) solution is to use a hash set
to store the values of the array as we iterate through it

each check if the value is already in the hash set and return true if it is
 """
class Solution:
    def containsDuplicate(self, nums:List[int]) ->bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False