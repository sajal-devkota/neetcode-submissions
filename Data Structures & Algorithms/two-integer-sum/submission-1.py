class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_index = {}
        for i_index in range (len(nums)):
            ans = target - nums[i_index]
            if ans in num_and_index :
                return [num_and_index.get(ans),i_index]
            else:
                num_and_index[nums[i_index]] = i_index