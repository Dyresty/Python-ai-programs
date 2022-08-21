from sys import exit

visited=[]
graph={'1':['2','3'],
       '2':['4','5'],
       '3':['6','7'],
       '4':[],
       '5':[],
       '6':[],
       '7':[]       
       }
print(graph)

key=input("Enter the element to be searched")
keyFlag=0
node='1'
count=0

def dfs(node,key):
    global count
    global keyFlag
    if keyFlag==1:
        exit
    count+=1
    if(node==key):
        print(node)
        visited.append(node)
        keyFlag=1
        exit
    if node not in visited:
        print(node)
        visited.append(node)
        for ele in graph[node]:
            dfs(ele,key)
            
x=dfs(node,key)
if keyFlag==0:
    print("Key element",key,"not found")
else:
    print("Key element",key,"found at count=",count)
print(visited)

