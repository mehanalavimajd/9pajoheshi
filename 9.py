open = []
close = []
s = input()
err = 0
for i in range(len(s)):
    if (err == 1):
        print("not correct")
        break ;
    c = s[i]
    if (c == "(" or c == "["):
        open.append(c)
    else:
        if (c == ')'):
            if (open[len(open)-1] == "("):
                open.pop()
            else: err = 1
        if c == ']':
            if (open[len(open)-1] == "["):
                    open.pop()
            else: err=1
if err==0:
    print("ok")
