def maxStrength(n, a[], k):
  if k==1:
    return max(a)
  if k==null or k==o:
    return 0
      
   max_s = 0
    for i in range(n):
        sum=a[i:i+k]
        if sum>max_s:
            max_s=sum
    return max_s
