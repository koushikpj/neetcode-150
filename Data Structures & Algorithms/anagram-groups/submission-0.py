class Solution:
    def __init__(self):
        self.hashTable = {}
    def groupAnagrams(self, strs) :
        for ch in strs:
            temp = "".join(sorted(ch))
            if temp not in self.hashTable:
                self.hashTable[temp] = [ch] 
                continue 
            else:self.hashTable[temp].append(ch) 
        result = list() 
        for i in self.hashTable.keys():
            if len(self.hashTable[i])>0:result.append(self.hashTable[i])
        return result



        