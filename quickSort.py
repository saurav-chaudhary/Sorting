def horePatition(arr, low, high):
    p = arr[low]
    i = low-1
    j = high+1
    while True:
        i = i +1
        while arr[i]<p:
            i = i+1
        j = j-1
        while arr[j]>p:
            j = j-1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]


def qSort(arr,low,high):
    if low<high:
        p = horePatition(arr,low,high)
        qSort(arr,low,p)
        qSort(arr,p+1,high)
    return arr
arr = [8,4,7,9,3,10,5]
l = 0
n = len(arr)
print(qSort(arr,l,n-1))
