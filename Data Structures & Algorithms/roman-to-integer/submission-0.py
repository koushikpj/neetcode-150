class Solution:
    def romanToInt(self, s):
        result = 0
        d1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i==len(s)-1:result+=d1[s[i]]
            else:
                if d1[s[i]]<d1[s[i+1]]:result-=d1[s[i]]
                else:result+=d1[s[i]]
        return result


        