M=int(input("Enter the number of vehicles:"))
N=int(input("Enter number of children: "))
x=M%N
if x==0:
    print("You are so lucky")
elif x!=0 and x%2!=0:
    print("Mr.Peter gets", x, "Vehicles")
elif x!=0 and x%2==0:
    print("Mr.Peter gets", x, "Vehicles. He is lucky")
