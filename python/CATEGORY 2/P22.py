text = input("Enter the String: ")
char= input("Enter the char: ")
newtext = ""
for i in range(len(text)):
    if text[i]!=char:
        newtext = newtext + text[i]

print("\nString after removing the char: ")
text = newtext
print(text)
