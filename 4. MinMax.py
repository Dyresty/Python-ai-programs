def minmax(d,node,maxP,v):
    global children,depth
    if d==depth:
        return v[node]
    if maxP:
        best=-999
        for i in range(0,children):
            value=minmax(d+1,node*children+i,False,v)
            best=max(best,value)
        return best
    else:
        best=999
        for i in range(0,children):
            value=minmax(d+1,node*children+i,True,v)
            best=min(best,value)
        return best
values=[]
children=int(input("Enter the no of children"))
depth=int(input("Enter the depth"))
for i in range(0,pow(children,depth)):
    y=int(input("Enter terminal node"))
    values.append(y)
print(values)
print("The optimal value is : ", minmax(0, 0,True, values))
