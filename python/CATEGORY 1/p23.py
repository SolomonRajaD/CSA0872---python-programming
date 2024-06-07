a=[[2,5,3],
   [6,4,1],
   [9,7,8]]
l=[]
for i in range(len(a[0])):
    l.append(a[0][i])
for j in range(1,len(a)-1):
    l.append(a[j][-1])
for k in range(1,len(a[-1])+1):
    l.append(a[-1][-k])
for m in range(len(a[0])-1):
    l.append(a[1][m])
print(l)
