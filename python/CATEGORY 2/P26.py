def removeKdigits(num,k):    
    stack = []
    for digit in num:
        while k > 0 and len(stack) > 0 and stack[-1] > digit:
            k -= 1
            stack.pop()  
        stack.append(digit)
    if k > 0:
        stack = stack[:-k]     
    return "".join(stack).lstrip("0") or "0"

num="143219"
k=2
print(removeKdigits(num,k))
