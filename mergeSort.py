def mergeSort(l,low,high):
    if high>low:
        mid = (low+high)//2
        mergeSort(l,low,mid)
        mergeSort(l,mid+1,high)
        merge(l,low,mid,high)
    return l
def merge(l,low,mid,high):
    left = l[low:mid+1]
    right = l[mid+1:high+1]
    i = 0
    j = 0
    k = low
    while i<len(left) and j < len(right):
        if left[i]<=right[j]:
            l[k] = left[i]
            k +=1
            i +=1
        else:
            l[k] = right[j]
            k +=1
            j +=1
    while i <len(left):
        l[k] = left[i]
        i +=1
        k +=1
    while j < len(right):
        l[k] = right[j]
        k +=1
        j +=1

    return l

l = [2,1,4,6,5,8,3]
print(mergeSort(l,0,len(l)))