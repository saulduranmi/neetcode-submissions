class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        needle = 0
        while needle <= length:
            needlenum = nums[needle]
            for i,num in enumerate(nums):
                if i != needle:
                    if (needlenum + num)==target:
                        return [needle, i]               
            needle = needle+1