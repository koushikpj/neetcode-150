class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = list() 
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:continue 
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:continue 
                val = self.TwoSum(nums,j+1,len(nums)-1,target-nums[i]-nums[j],nums[i],nums[j])
                if len(val)!=0:result.extend(val)
        return result
    def TwoSum(self,nums,start,end,target,first,seacond):
        temp = list()
        while start<end:
            val = nums[start]+nums[end]
            if val>target:end-=1
            if val<target:start+=1 
            if val==target:
                temp.append([first,seacond,nums[start],nums[end]])
                start+=1 
                end-=1 
                while start<end and nums[start]==nums[start-1]:start+=1 
                while start<end and nums[end]==nums[end+1]:end-=1
        return temp

        