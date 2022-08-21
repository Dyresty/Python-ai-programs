visited=[]
queue=[]

graph={'1':['2','3'],
       '2':['4','5'],
       '3':['6','7'],
       '4':[],
       '5':[],
       '6':[],
       '7':[],
       }

print(graph)
ch='1'
while ch!='0':
    ch=(input("Enter 1 to enter a fresh node\n2 to add links to a new node\n3 to add links to existing node\n4 to display\n0 to continue to bfs\n"))
    if ch=='1':
        a=(input("Enter the node"))
        graph[a]=None
    elif ch=='2':
        b=(input("Enter the node"))
        graph[b]=None
        b=[]
        app=(input("Enter link"))
        b.append(app)
        graph[a]=b
    elif ch=='0':
        continue
    elif ch=='4':
        print(graph)
    else:
        print("Wrong input")

i=0
key=input("Enter the element being searched")
keyFlag=0
node='1'

def bfs(node, key):
    count=1
    if(node==key):
        return count
    visited.append(node)
    queue.append(node)
    while queue:
        popped=queue.pop(0)
        for ele in graph[popped]:
            count=count+1
            if int(ele)==int(key):
                visited.append(ele)
                return count
            elif ele not in visited:
                visited.append(ele)
                queue.append(ele)
    str='-1'
    return str;

x=bfs(node,key)
if x=='-1':
    print("Key element",key,"not found")
else:
    print("Key element",key,"found at count=",x)

    