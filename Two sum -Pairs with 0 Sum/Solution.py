
def getPairs(arr):
    # code here
    arr.sort()
    
    pointer1 = 0 
    pointer2 = len(arr)-1
    res = []
    while pointer1<pointer2:
        if arr[pointer1]+arr[pointer2] ==0:
            res.append([arr[pointer1],arr[pointer2]])
            pointer1 += 1
            pointer2 -=1
            
            while pointer1 < pointer2 and arr[pointer1] == arr[pointer1 - 1]:
                pointer1+= 1

            while pointer1 < pointer2 and arr[pointer2] == arr[pointer2 + 1]:
                pointer2 -= 1
            
        elif arr[pointer1]+arr[pointer2]<0:
            pointer1 +=1
        elif arr[pointer1]+arr[pointer2]>0:
            pointer2 -=1
    res = list(res)
            
    return res
    