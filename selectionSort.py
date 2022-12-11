def selection(l):
    n = len(l)
    for i in range(n-1):
        x = i
        for j in range(i+1,n):
            if l[j]<l[x]:
                x = j
        l[i],l[x] = l[x],l[i]
    return l

l = [2,4,1,6,5,8]
print(selection(l))
