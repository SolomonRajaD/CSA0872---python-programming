n="A man, a plan, a canal: Panam"
s=n.lower()
text=''
for i in s:
    if i.isalpha():
        text+=i
x=text[::-1]
if(x==text):
    print("Valid Palindrome")
else:
    print("Invalid Palindrome")
