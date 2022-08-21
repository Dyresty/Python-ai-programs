def solve(enemy, tables):
    for i in enemy:
        if i in tables:
            return False
    return True
n = int(input("Number of People: "))
c = int(input("Number of tables: "))
enemy = {}
tables = {}
for i in range(c):
    tables[i] = []
for i in range(n):
    enemy[i] = []
print("Give the enemy list:(Type exit for exit)")
while(True):
    string = input()
    if(string == "exit"):
        break
    a, b = map(int, string.split())
    enemy[a].append(b)
    enemy[b].append(a)
print(enemy)

flag1 = True
for i in range(n):
    flag = False
    for j in range(c):
        print(str(i)+ " " + str(j) + " " + str(solve(enemy[i],tables[j])))
        if solve(enemy[i],tables[j]):
            tables[j].append(i)
            flag = True
            break

    if flag == False:
        print("False")
        flag1 = False
        break
if flag1:
    print(tables)
