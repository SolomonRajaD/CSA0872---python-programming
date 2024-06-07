def strStr(haystack,needle):
    l=[]
    if needle==" ":
        return 0
    else:
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                if haystack[i:i+len(needle)]==needle:
                    l.append(i)
                    continue
                else:
                    return -1
        return l

# Driver Program

haystack="sadsad"
needle="sad"
print(strStr(haystack,needle))
