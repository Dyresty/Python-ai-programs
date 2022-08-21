visited=[]
frontier=[]
flag=0
graph={
        'Arad':{'Zerind':75,'Sibiu':140,'Timisoara':118},
        'Zerind':{'Oradea':71},
        'Oradea':{'Sibiu':151},
        'Timisoara':{'Lugoj':111},
        'Sibiu':{'Fagaras':99,'Rimnicu Vilcea':80},
        'Lugoj':{'Mehadia':70},
        'Fagaras':{'Bucharest':211},
        'Rimnicu Vilcea':{'Pitesti':97,'Craiova':146},
        'Mehadia':{'Dobreta':75},
        'Bucharest':{'Pitesti':101,'Urziceni':85,'Giurglu':90},
        'Pitesti':{'Craiova':138,'Bucharest':101},
        'Craiova':{'Dobreta':120},
        'Dobreta':{},
        'Urziceni':{'Hirsova':98,'Vaslui':142},
        'Hirsova':{'Eforie':86},
        'Vaslui':{'Lasi':92},
        'Lasi':{'Neamt':87},
        'Giurglu':{},
        'Eforie':{}
}

from operator import itemgetter
frontier.sort(key=itemgetter(1))

start='Arad'
dest='Bucharest'

def ucs(node,dest):
    global visited, frontier, queue, flag, graph, fcost
    ccost=0
    frontier.append((start,ccost))
    while flag==0:
        node=frontier[0][0]
        ccost=frontier[0][1]
        print(frontier)
        frontier.remove((node,ccost))
        visited.append(node)
        if node==dest:
            flag=1
            fcost=ccost
            return fcost
        else:
            for a in graph[node]:
                if a not in visited:
                    frontier.append((a,ccost+graph[node][a]))
        frontier.sort(key=itemgetter(1))
fcost=ucs(start,dest)
print(fcost)
