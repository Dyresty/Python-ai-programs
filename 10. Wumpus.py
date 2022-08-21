'''
Write a python program to implement The Wumpus world problem. The problem deals with an AI robot
navigating its way through a 4x4 puzzle to try and find gold. The robot must safely navigate its way
around bottomless pits of death and evil Wumpus creatures to locate the gold hidden on the board. After
it has successfully found the gold, it must safely navigate its way back to the starting point. The robot
must use its light sensors and the signals sent to it at each square to determine which way to properly
navigate to reach its goal.
'''
#w1 wumpus, s10 stench, p100 pit, b1000 breeze, g10000 gold, x1000000 sparkle 
#1p for pit, 2b for breeze, 3w for wumpus, 4s for stench, 5g for gold, 6x for sparkle
import random

world = [[0]*4 for n in range(4)]
world_descy = [['N']*4 for n in range(4)]
options=[]

#wumpus location
wumpus_done=0
pit_done=0
gold_done=0

def wumpus():    
    x=random.randint(0,3)
    y=random.randint(0,3)
    if x==0 and y==0:
        return 0
    if world[x][y]==0:
        world[x][y]+=1
        world_descy[x][y]=world_descy[x][y]+'W'
        if(x+1!=4):
            world[x+1][y]+=10
            world_descy[x+1][y]=world_descy[x+1][y]+'S'
        if(x-1!=-1):
            world[x-1][y]+=10
            world_descy[x-1][y]=world_descy[x-1][y]+'S'
        if(y+1!=4):
            world[x][y+1]+=10
            world_descy[x][y+1]=world_descy[x][y+1]+'S'
        if(y-1!=-1):
            world[x][y-1]+=10
            world_descy[x][y-1]=world_descy[x][y-1]+'S'
        return 1
    else:
        return 0
    
def pit():    
    x=random.randint(0,3)
    y=random.randint(0,3)
    if x==0 and y==0:
        return 0
    if world[x][y]==0:
        world[x][y]+=100
        world_descy[x][y]=world_descy[x][y]+'P'
        if(x+1!=4):
            world[x+1][y]+=1000
            world_descy[x+1][y]=world_descy[x+1][y]+'B'
        if(x-1!=-1):
            world[x-1][y]+=1000
            world_descy[x-1][y]=world_descy[x-1][y]+'B'
        if(y+1!=4):
            world[x][y+1]+=1000
            world_descy[x][y+1]=world_descy[x][y+1]+'B'
        if(y-1!=-1):
            world[x][y-1]+=1000
            world_descy[x][y-1]=world_descy[x][y-1]+'B'
        return 1
    else:
        return 0
    
def gold():    
    x=random.randint(0,3)
    y=random.randint(0,3)
    if x==0 and y==0:
        return 0
    if world[x][y]==0:
        world[x][y]+=10000
        world_descy[x][y]=world_descy[x][y]+'G'
        if(x+1!=4):
            world[x+1][y]+=100000
            world_descy[x+1][y]=world_descy[x+1][y]+'X'
        if(x-1!=-1):
            world[x-1][y]+=100000
            world_descy[x-1][y]=world_descy[x-1][y]+'X'
        if(y+1!=4):
            world[x][y+1]+=100000
            world_descy[x][y+1]=world_descy[x][y+1]+'X'
        if(y-1!=-1):
            world[x][y-1]+=100000
            world_descy[x][y-1]=world_descy[x][y-1]+'X'
        return 1
    else:
        return 0

'''
def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums
'''

def world_desc():
    for i in range(4):
        for j in range(4):
            print(world_descy[i][j],end='\0')
        print("\n")
            
def Options_call(x,y):
    if 'O' in world_descy[x][y]:
      temp=world_descy[x][y].replace('O','V') 
      world_descy[x][y]=temp
    if(x+1!=4 and 'V' not in world_descy[x+1][y]):
            world_descy[x+1][y]=world_descy[x+1][y]+'O'
    if(x-1!=-1 and 'V' not in world_descy[x-1][y]):
            world_descy[x-1][y]=world_descy[x-1][y]+'O'
    if(y+1!=4 and 'V' not in world_descy[x][y+1]):
            world_descy[x][y+1]=world_descy[x][y+1]+'O'
    if(y-1!=-1 and 'V' not in world_descy[x][y-1]):
            world_descy[x][y-1]=world_descy[x][y-1]+'O'

while wumpus_done==0:
    wumpus_done=wumpus()
    
while pit_done==0:
    pit_done=pit()
    
while gold_done==0:
    gold_done=gold()
    
    
world_descy[0][0]=world_descy[0][0]+'O'
life=1
x=0
y=0
print("Welcome to Wumpus world.\nThere is one wumpus, one pit and one gold bar in this cave\n")
print("B indicates Breeze\nP indicates Pit\nS indicates Stench\nW indicates Wumpus\nX indicates glitter\nG indicates Gold\nN indicates default_value\nO for Option to visit")

print("You start at",x,',',y,"-",world_descy[x][y])
print("\n")
Options_call(x,y)
while(life==1):
    print("You can proceed to ")
    
    for i in range(4):
        for j in range(4):
            if 'O' in world_descy[i][j]:
                print(i,',',j)
                
    i=int(input("Enter the row value"))
    j=int(input("Enter column value"))
    if (i>3 or i<0) and (j>3 or j<0):
        print("\nENTER THE CORRECT INPUT\n")
        continue
    x=i
    y=j
    
    if('O' not in world_descy[x][y]):
        print("\nENTER THE CORRECT INPUT\n")
        continue
    
    Options_call(x,y)
    print('Your location is now',x,',',y,'-',world_descy[x][y])        
    if('W' in world_descy[x][y]):
        print("Wumpus has eaten you")
        life=0
    elif('P' in world_descy[x][y]):
        print("Pit has eaten you")
        life=0
    elif('G' in world_descy[x][y]):
        print("Gold found")
        life=2
        print("Game won")
        
        
    