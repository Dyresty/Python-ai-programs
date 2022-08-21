ttable=[
    [1,1,1],
    [1,-1,1],
    [-1,1,1],
    [-1,-1,1]
]

target = [1,-1,-1,-1]

w1=0
w2=0
b=0
theta=0
alpha=1

w11=0
w21=0
b1=0

bc=0

while bc==0:
    for i in range(0,4):
        yin = ttable[i][0]*w1+ ttable[i][1]*w2 + ttable[i][2]*b
        y=0
        if yin>theta:
            y=1
        elif -theta<=yin<theta:
            y=0
        else:
            y=-1
        if (ttable[i][0]!=0 and ttable[i][1]!=0) and target[i]!=y:
            w1=w1+alpha*target[i]*ttable[i][0]
            w2=w2+alpha*target[i]*ttable[i][1]
            b=b+alpha*target[i]*ttable[i][2]
        print(w1,w2,b)
        if(w11==w1 and w2==w21 and b==b1):
            bc=1
    w11=w1
    w21=w2
    b1=b
