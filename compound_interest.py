def comp(p,t,r):
    if t==0:
        return p
    else:
        return comp(p+(p*r)/100,t-1,r)
a=int(input("Enter principle:"))
b=int(input("Enter the rate"))
c=int(input("Enter the time:"))
print(comp(a,c,b))