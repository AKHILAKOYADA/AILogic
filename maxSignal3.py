def maxStrength(n, a[], k):
    max_s = 0
    for i in range(n-2):
        sum=a[i:i+k]
        if sum>max_s:
            max_s=sum
    return max_s
