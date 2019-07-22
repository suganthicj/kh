X11,Y11=map(str,input().split())
for p in range(len(Y11)):
    if(X11.count(X11[p])==Y11.count(Y11[p])):
        print("yes")
        break
    else:
        print("no")
        break
