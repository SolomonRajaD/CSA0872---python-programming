def removeCommonWords(s1,s2):
  com=[]
  sent1=list(s1.split())
  sent2=list(s2.split())
  for i in sent1:
    if i in sent2:
      sent1.remove(i)
      sent2.remove(i)
      com.append(i)
      continue
  print(*sent1)
  print(*sent2)
  print("common words",*com)
sentence1 = input("Enter string1: ")
sentence2 = input("Enter string2: ")
removeCommonWords(sentence1,sentence2)
