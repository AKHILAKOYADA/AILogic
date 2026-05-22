def maxLen(str):
  if(len[str]==1):
    return str
  maxlen=[]
  for i in range(len[str]-1):
    m=str[i]
      if str[i]!=str[i+1]:
        m+=str[i+1]
    maxlen.append(len[m])
  return max(maxlen)
