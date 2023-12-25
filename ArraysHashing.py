#First page of algorithms practice in neetcode's Blind 75

#First problem is an easy rated problem checking if the input list nums contains  any duplicate numbers
#This submission ran in 435ms and used 28.18 MB of memory

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                return True
        return False