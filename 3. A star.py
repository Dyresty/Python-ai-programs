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

h_value = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsowa": 151,
    "Lasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
}

c_cost = {
    "Arad": 0,
    "Bucharest": 0,
    "Craiova": 0,
    "Dobreta": 0,
    "Eforie": 0,
    "Fagaras": 0,
    "Giurgiu": 0,
    "Hirsowa": 0,
    "Lasi": 0,
    "Lugoj": 0,
    "Mehadia": 0,
    "Neamt": 0,
    "Oradea": 0,
    "Pitesti": 0,
    "Rimnicu Vilcea": 0,
    "Sibiu": 0,
    "Timisoara": 0,
    "Urziceni": 0,
    "Vaslui": 0,
    "Zerind": 0,
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
                    c_cost[a]=c_cost[node]+graph[node][a]
                    frontier.append((a,c_cost[a]+int(h_value[a])))
        frontier.sort(key=itemgetter(1))
fcost=ucs(start,dest)
print(fcost)
