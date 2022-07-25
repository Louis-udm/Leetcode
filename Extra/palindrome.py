
# Palindrome: word, phrase, or sequence that reads the same backward as forward, e.g., madam or nursesrun.
# Given a string, find the longest substring which is palindrome. For example, if the given string is “isevilolivealive”, the output should be “evilolive”.

str1="aamadamb"
str2="isevilolivealive" 
def palin(st):
    i=0
    tmp=""
    results=[]
    while i<len(st):
        j=len(st)-1
        while j>-1:
            # print(i,j)
            if st[i]==st[j]:
                m=i
                n=j
                while m<len(st)-1 and n>-1:
                    if st[m]==st[n]:
                        tmp+=st[m]
                        m+=1
                        n-=1
                    else:
                        break
                results.append(tmp)
                tmp=""
            j-=1
        i+=1
    # print(results)
    results.append(tmp)

    return max(results,key=len) # return the longest str in results.

print(palin(str1))
print(palin(str2))
