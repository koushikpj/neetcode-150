class Solution:
    def __init__(self):
        self.hashTable = {}
    def twoSum(self, nums, target):
        for i in range(len(nums)):self.hashTable[nums[i]]=i 
        for i in range(len(nums)):
            if target-nums[i] in self.hashTable:
                if target-nums[i]!=nums[i]:return [i,self.hashTable[target-nums[i]]] 
                else:
                    if nums.count(nums[i])>1:return [i,self.hashTable[nums[i]]]