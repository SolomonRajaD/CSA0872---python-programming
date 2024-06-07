string=input(“Enter the Para: ”)
str1=string.split(" ...")
str1.pop()
print("Total number of lines:",len(str1))
count=0
for i in str1:
    str2=i.split()
    #print(str2)
    for j in str2:
        if j[0]=="B":
            count=count+1
print("Number of Sentences that start with letter B :",count)
