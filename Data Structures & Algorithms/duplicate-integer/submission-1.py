class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         a = set()
         for i in range(len(nums)):
            a.add(nums[i])
            
         if len(nums) == len(a):
            return False
         else:
            return True
        