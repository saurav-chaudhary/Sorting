def countInv(arr,low,high):
    res = 0
    if low < high:
        mid = (low+high)//2
        res += countInv(arr,low,mid)
        res +=countInv(arr,mid+1,high)
        res += countMerge(arr,low,mid,high)
    return res
def countMerge(arr,low,mid,high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    res,i,j,k = 0,0,0,low

    while i <len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k]= right[j]
            res += len(left)-i
            j +=1
        k +=1
    while i < len(left):
        arr[k] = left[i]
        i +=1
        k+=1
    while j< len(right):
        arr[k] = right[j]
        j +=1
        k +=1
    return res

arr = [2,4,1,3,5]
n = len(arr)
print(countInv(arr,0,n))
