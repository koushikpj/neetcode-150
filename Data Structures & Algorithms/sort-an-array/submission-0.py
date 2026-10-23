class Solution:
    def sortArray(self, nums):
        val = self.MergeSort(nums,0,len(nums)-1) 
        return val 
    def MergeSort(self,arr,start,end):
        if start<end:
            mid = (start+end)//2 
            self.MergeSort(arr,start,mid)
            self.MergeSort(arr,mid+1,end)
            self.Merge(arr,start,end,mid)
        return arr 
    def Merge(self,arr,start,end,mid):
        left = arr[start:mid+1]
        right = arr[mid+1:end+1] 
        i,j = 0,0 
        k = start 
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1 
                k+=1 
            else:
                arr[k] = right[j] 
                j+=1 
                k+=1 
        while i<len(left):
            arr[k] = left[i]
            i+=1 
            k+=1 
        while j<len(right):
            arr[k] = right[j] 
            k+=1 
            j+=1  
if __name__ == "__main__":
    obj = Solution() 
    print(obj.sortArray([10,9,8,7,6,5,4,3,2,1]))
        


        