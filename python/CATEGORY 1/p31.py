def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
 
# Driver program
s = int(input("Enter the value of n: "))
print ("Number of ways = ", end="")
print (fib(s+1))
