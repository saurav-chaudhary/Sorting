def horePartition(arr,low,high):
    p = arr[low]
    i = low-1
    j = high+1
    while True:
        i = i+1
        while arr[i]<p:
            i = i+1
        j = j-1
        while arr[j]>p:
            j = j-1
        if i>=j:
            return j
        arr[i],arr[j]= arr[j],arr[i]
arr = [8,4,7,9,3,10,5]
l = 0
n = len(arr)
print(horePartition(arr,l,n-1))
