class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:return 0
        nums = list(set(nums))
        nums.sort() 
        max_len = 0 
        temp = 1
        for i in range(len(nums)):
            if i==0:continue 
            else:
                if nums[i]-1 == nums[i-1]:temp+=1 
                else:
                    if temp>max_len:
                        max_len = temp 
                        temp = 1 
                    else:temp = 1 
        if temp>max_len:max_len=temp
        return max_len