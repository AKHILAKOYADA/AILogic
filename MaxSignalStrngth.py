def maxStrength(n, a[], k):
    max_s = 0
    for i in range(n):
        sum=a[i:i+k]
        if sum>max_s:
            max_s=sum
    return max_s
res=maxStrength(6,[2,1,5,1,3,2],3)
