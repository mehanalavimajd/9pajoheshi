num = int(input())
numCopy = num
rev = 0
while (num > 0):
    rev = num % 10+(10*rev)
    num //= 10
if(rev==numCopy):
    print("palindrome")
else:
    print("not palindrome")
