ttable=[
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

ch='1'
while ch!='5':
    ch=input("Enter 1 for AND\n2 for OR\n3 for ANDNOT\n4 for XOR\n5 to exit")
    if ch=='1':
        answer=[]
        answertt=[]
        for i in range (0,4):
            answer.append(ttable[i][0]*1+ttable[i][1]*1)
        for i in range(0,4):
            if answer[i]>=2:
                answertt.append(True)
            else :
                answertt.append(False)
        print(answer)
        print(answertt)
    if ch=='2':
        answer=[]
        answertt=[]
        for i in range (0,4):
            answer.append(ttable[i][0]*1+ttable[i][1]*1)
        for i in range(0,4):
            if answer[i]>=1:
                answertt.append(True)
            else :
                answertt.append(False)
        print(answer)
        print(answertt)
    if ch=='3':
        answer=[]
        answertt=[]
        for i in range (0,4):
            answer.append(ttable[i][0]*1+ttable[i][1]*-1)
        for i in range(0,4):
            if answer[i]>=1:
                answertt.append(True)
            else :
                answertt.append(False)
        print(answer)
        print(answertt)
    if ch=='4':
        answerz1=[]
        answerttz1=[]
        for i in range (0,4):
            if (ttable[i][0]*1+ttable[i][1]*-1)>=1:
                answerz1.append(1)
            else:
                answerz1.append(0)
        for i in range(0,4):
            if answerz1[i]>=1:
                answerttz1.append(True)
            else:
                answerttz1.append(False)
        print(answerz1)
        print(answerttz1)

        answerz2=[]
        answerttz2=[]
        for i in range (0,4):
            if (ttable[i][0]*-1+ttable[i][1]*1)>=1:
                answerz2.append(1)
            else:
                answerz2.append(0)
        for i in range(0,4):
            if answerz2[i]>=1:
                answerttz2.append(True)
            else:
                answerttz2.append(False)
        print(answerz2)
        print(answerttz2)

        answer=[]
        answertt=[]
        for i in range (0,4):
            answer.append(answerz1[i]*1+answerz2[i]*1)
        for i in range(0,4):
            if answer[i]>=1:
                answertt.append(True)
            else :
                answertt.append(False)
        print(answer)
        print(answertt)
