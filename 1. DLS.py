visited=[]
result=[]
depth=-1
flag = 0
graph = {
    '1':['2','3'],
    '2':['4','5'],
    '3':['6','7'],
    '4':['8','9'],
    '5':[],
    '6':[],
    '7':[],
    '8':['10'],
    '9':[],
    '10':[]
}

def dls(node,key):
    global flag,depth,visited,result,limit
    visited.append(node)
    depth+=1
    if(node==key):
        print("Node found")
        flag=1
    else:
        for a in graph[node]:
            if flag==0 and a not in visited and depth<limit:
                dls(a,key)
                depth-=1
    if flag==1:
        result.append(node)


start=input("Enter the starting node")
key=input("Enter key node")
limit=int(input("Enter the depth limit"))
dls(start,key)
if flag==0:
    print("Node not found")
else:
    result.reverse()
    print(result)
