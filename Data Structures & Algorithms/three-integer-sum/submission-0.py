class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = [] 
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:continue 
            val = self.TwoSum(nums,i+1,len(nums)-1,-nums[i])
            if len(val)!=0:result.extend(val) 
        return result
    def TwoSum(self,nums,start,end,target):
        temp = []
        while start<end:
            sum = nums[start]+nums[end]
            if sum>target:end-=1 
            if sum<target:start+=1 
            if sum==target:
                temp.append([-target,nums[start],nums[end]])
                start+=1 
                end-=1 
                while start<end and nums[start]==nums[start-1]:start+=1 
                while start<end and nums[end]==nums[end+1]:end-=1 
        return temp
                      
        