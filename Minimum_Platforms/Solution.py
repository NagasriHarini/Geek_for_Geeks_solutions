class Solution:    
    def minPlatform(self, arr, dep):
        
        arr.sort()
        dep.sort()
        
        n = len(arr)
        
        i = 1
        j = 0 
        
        platforms = 1
        max_plat = 1
        
        while i<n and j<n:
            if arr[i] <dep[j]:
                platforms +=1
                i+=1
            else:
                platforms -=1
                j +=1
                
            max_plat = max(max_plat, platforms)
            
            
        return max_plat