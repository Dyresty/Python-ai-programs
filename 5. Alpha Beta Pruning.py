from math import inf
alpha=-inf
beta=+inf
children=2
depth=3

def alphabeta(d,node,maxP,v,alpha,beta):
    global children,depth

    if d==depth:
        return v[node]
    if maxP:
        best=alpha
        for i in range(0,children):
            value=alphabeta(d+1,node*children+i,False,v,alpha,beta)
            best=max(best,value)
            alpha=max(best,alpha)
            if alpha >= beta:
                break
        return best
    else:
        best=beta
        for i in range(0,children):
            value=alphabeta(d+1,node*children+i,True,v,alpha,beta)
            best=min(best,value)
            beta=min(best,beta)
            if alpha >= beta:
                break
        return best
values=[]
x=int(input("Enter the number of terminal nodes"))
depth=int(input("Enter depth value"))
for i in range(0,x):
    y=int(input("Enter terminal node"))
    values.append(y)
print(values)
print("The optimal value is : ", alphabeta(0, 0,True, values, alpha, beta))

#You can count number of prunes  by placing a variable inside alpha <= beta
