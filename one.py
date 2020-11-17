def facorial(x):
    if x==0:
        return 1
    ans=x*facorial(x-1) 
    return ans 

s=facorial(5)
print(s)
