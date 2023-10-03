f=False
def isprime(n):
    if(n==1):
        return False
    f=False
    for i in range(2,n):
       if(f==True):
            return False
       if(n%i==0):
        f=True
    return True
a=int(input())
b=int(input())
print("-----")
for i in range(a+1,b):
    if(isprime(i)):
        print(i)