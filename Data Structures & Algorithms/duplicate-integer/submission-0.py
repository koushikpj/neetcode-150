class Solution:
    def hasDuplicate(self, nums: List[int]):
        return len(set(nums))!=len(nums)
        