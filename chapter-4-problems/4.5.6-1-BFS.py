R, C = map(int, input().split())
StartX, StartY = map(int, input().split())
GoalX, GoalY = map(int, input().split())

maze = [ [ None ] * C for _ in range(R) ]

for i in range(R):
    array = input()
    maze[i] = list(array)

# insert nodes into A and B
A = []
B = []

for i in range(R - 1):
    for j in range(C - 1): # C - 1 = 3 - 1 = 2
        if maze[i][j] == ".":
            if maze[i][j + 1] == ".":
                a =  i * C  + j + 1
                b =  i * C  + j + 2
                A.append(a)
                B.append(b)

            if maze[i + 1][j] == ".":
                a =  i * C  + j + 1
                b = ( i + 1 ) * C  + j + 1
                A.append(a)
                B.append(b)

# create adjacency list
G = [ list() for _ in range( R * C + 1) ]
for i in range(len(A)):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

# BFS
import queue

dist =[  -1  for _ in range( R * C + 1 ) ]
Q = queue.Queue()
dist[( StartX - 1 ) * C + ( StartY - 1 )+ 1 ] = 0
Q.put( ( StartX - 1 ) * C + ( StartY - 1 )+ 1 )


while not Q.empty():
    pos = Q.get()
    for i in G[pos]:
        if dist[i] == -1:
            dist[i] = dist[pos] + 1
            Q.put(i)

print(dist[( GoalX - 1 ) * C + ( GoalY - 1 )+ 1 ])
