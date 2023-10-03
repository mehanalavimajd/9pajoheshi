
a = int(input())
b = int(input())
c = int(input())
if a >= 100 or b >= 100 or c >= 100:
    print("error")
else:
    print('a*b and a+b:')
    print(str(a*b) + "\t"+ str(a+b))
    print('a*c and a+c:')
    print(str(a*c) + "\t"+ str(a+c))
    print('c*b and c+b:')
    print(str(c*b) + "\t" + str(c+b))
