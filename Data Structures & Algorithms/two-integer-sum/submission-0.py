class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index in range (len(nums)):
            for j_index in range(i_index+1, len(nums)):
                if nums[i_index]+nums[j_index] == target:
                    return [i_index,j_index]