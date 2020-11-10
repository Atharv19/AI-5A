import math

maze = []
path = []
closedPath = []
neigbhours = [[1,1],[0,1],[1,0],[1,-1],[0,-1],[-1,1],[-1,0],[-1,-1]]

def euclidDist(x,n,m):
    dist = math.sqrt((n-1-x[0])*2+(m-1-x[1])*2)
    return dist

def findShortestPath(nextPath,n,m):
    minDistance = 999
    next = []
    for x in nextPath:
        if(euclidDist(x,n,m) < minDistance):
            minDistance = euclidDist(x,n,m)
            next = x

    return next

def findPath(n,m,dest):
    path.append([0,0])

    current = [0,0]

    while(current != dest):
        nextPath = []
        for x in neigbhours:
            a = []
            a.append(current[0]+x[0])
            a.append(current[1]+x[1])
            if a[0]>-1 and a[0]<n and a[1]>-1 and a[1]<m:
                if(maze[a[0]][a[1]]):
                    if a not in path and a not in closedPath: 
                        nextPath.append(a)

        if(nextPath):   
            current = findShortestPath(nextPath,n,m)
            path.append(current)
        else:
            if path:
                closedPath.append(current)
                path.pop()
                if path: 
                    current = path[len(path)-1]
                else:
                    print("NO PATH")
                    exit(0)
            else:
                print("NO PATH")
                exit(0)

def start():
    n = int(input("\nEnter number of rows: "))
    m = int(input("\nEnter number of cols: "))
    print("give co-ordinates of destination")
    x= int(input())
    y= int(input())
    dest=[]
    dest.append(x)
    dest.append(y)
    
    print("\nEnter the maze structure: (0-blocked,1-free): ")

    for i in range(n):
        a = []
        a = list(map(int, input().split(" ")))
        maze.append(a)

    print("\n\n this is the MAZE")
    for i in range(n):
        for j in range(m):
            print(maze[i][j], end=" ")
        print()

    findPath(n,m,dest)

    print("\n this is the PATH")
    for i in range(n):
        for j in range(m):
            if([i,j] in path):
                print("-",end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

    print()
    print(path)

if __name__ == "__main__":
    start()