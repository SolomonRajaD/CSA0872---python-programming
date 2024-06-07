def findKthNumber(m, n, k):
        
    low = 1
    high = n*m
        
    while low < high:
        mid = (low + high) // 2
        count = 0
        for i in range(1, m+1):
            count += min(n, mid//i)
        if count < k:
            low = mid + 1
        else:
            high = mid
    return low

#Driver Program
m=3
n=3
k=5
print(findKthNumber(m,n,k))
