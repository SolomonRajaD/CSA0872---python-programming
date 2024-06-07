#Python code to Count Alphabets, Special character Numeric values and space 
string=input("Please enter a string: ")#take input from the user 
alphabets,num,special,space=0,0,0,0;#variable declaration and initilization
a=[]
d=[]
spl=[]
for i in range(len(string)): 
  if(string[i].isalpha()): #check Alphabets letters 
      #print(string[i],end="")
      alphabets+=1
      a.append(string[i])
  elif(string[i].isdigit()):#check numeric value 
      #print(string[i],end="")
      num+=1
      d.append(string[i])
  elif(string[i].isspace()):#check space 
      space+=1 
  else: 
      #print(string[i],end="")
      special+=1
      spl.append(string[i])
print("Alpabets letters: ",alphabets, a) 
print("\nnumbers: ",num, d) 
print("\nSpace: ",space) 
print("\nSpecial characters: ",special, spl)
