def facorial(x):
    if x==0:
        return 1
    c=x*facorial(x-1) 
    return c 

s=facorial(5)
print(s)
