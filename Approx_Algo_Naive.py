import random
import time
Naive_l = []
input_l =[]
ApproxAlgo_l = []

for V in range(1, 10):

  l2=[]
  for i in range(V):
      l3 = []
      for j in range(V):
          if i == j:
              l3.append(0)
          else :
              l3.append(1)
      l2.append(l3)

  a = random.randint(3, 30)
  w = l2

  for i in range(V):
    for j in range(i,V):
      if i != j:
        w[i][j]=random.randint(a, 2*a - 1)
        w[j][i]=w[i][j]

  G = []
  graph = []
  input_l.append(V)
  for i in range(V):
      l=[]
      for j in range(V):
          if w[i][j]!=0:
              l.append(1)
              G.append([i,j,w[i][j]])
          else:
              l.append(0)
      graph.append(l)
  
  Naive_start = time.time()

  def isSafe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
      return False
    for i in range(pos):
      if path[i] == v:
        return False
    return True

  hasCycle = False
  minwtsum=[]
  minwt=[]
  vertexlist=[]

  def hamCycle(graph):
    global hasCycle
    hasCycle = False
    path = []
    path.append(0)
    visited = [False]*(len(graph))

    for i in range(len(visited)):
      visited[i] = False

    visited[0] = True
    FindHamCycle(graph, 1, path, visited)
    if hasCycle:
      print("No Hamiltonian Cycle" + "possible ")
      return


  def FindHamCycle(graph, pos, path, visited):

    if pos == len(graph):
      if graph[path[-1]][path[0]] != 0:
        path.append(0)
        for i in range(len(path)):
          vertexlist.append(path[i])

          if(i<len(path)-1):
            minwt.append(w[path[i]][path[i+1]])

        minwtsum.append(sum(minwt))
        path.pop()
        hasCycle = True

      return

    for v in range(len(graph)):
      if isSafe(v, graph, path, pos) and not visited[v]:
        path.append(v)
        visited[v] = True
        FindHamCycle(graph, pos + 1, path, visited)
        visited[v] = False
        path.pop()

  hamCycle(graph)
  if(len(minwt)!=0):
      l=[]
      for i in range(0, len(minwt), V):
          q = minwt[i:i+V]
          q.append(sum(q))
          l.append(q)

      minimum = min(minwtsum)
      l1=[]

      for i in range(0, len(vertexlist), V+1):
          q = vertexlist[i:i+V+1]
          l1.append(q)
  Naive_end = time.time()
  t = Naive_end - Naive_start
  Naive_l.append(t * 1000)

  Start_t = time.time()
  def search(p, i):
      if p[i] == i:
          return i
      return search(p, p[i])

  def Insert(p, position, x, y):
          a = search(p, x)
          b = search(p, y)
          if position[a] < position[b]:
              p[a] = b
          elif position[a] > position[b]:
              p[b] = a
          else:
              p[b] = a
              position[a] += 1

  tree_size = 0
  kruskal_mst=[]
  def Kruskal(G, v):
          result = []
          i, e = 0, 0
          global tree_size
          graph = sorted(G, key=lambda item: item[2])
          p = []
          position = []
          for node in range(v):
              p.append(node)
              position.append(0)
          while e < v - 1:
              u, v1, w = graph[i]
              i = i + 1
              x = search(p, u)
              y = search(p, v1)
              if x != y:
                  e = e + 1
                  result.append([u, v1, w])
                  Insert(p, position, x, y)
          for u, v1, weight in result:
              kruskal_mst.append([u,v1,weight])

          global mst
          mst=[]
          for i in range(V):
              l=[]
              for j in range(V):
                  l.append(0)
              mst.append(l)
          for u, v, weight in result:
              
              mst[u][v]=1
              mst[v][u]=1
              tree_size += weight
          
          return tree_size
      
  Kruskal(G, V)

  def dfs(graph,vertex,path=[]):
          path+=[vertex]
          for neighbor in graph[vertex]:
              if neighbor not in path:
                  path=dfs(graph,neighbor,path)
          return path

  Ham_l=[]
  def MinHam_ApproxAlgo():
      al= {} 
      for x, row in enumerate(mst):
          al[x+1]=[]
          for i, v in enumerate(row):
              if v== 1 and i!=x:
                  al[x+1].append(i+1)
      l=dfs(al, 1)

      cost=0
      for i in range(V-1) :
          cost+=w[l[i]-1][l[i+1]-1]
          Ham_l.append([l[i]-1, l[i+1]-1, w[l[i]-1][l[i+1]-1]])
      
      cost+=w[l[V-1]-1][0]
      Ham_l.append([l[V-1]-1, l[0]-1, w[l[V-1]-1][l[0]-1]])

  MinHam_ApproxAlgo()
  End_t = time.time()
  t = End_t - Start_t
  ApproxAlgo_l.append(t*1000)


import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.plot(input_l, Naive_l)
plt.plot(input_l, ApproxAlgo_l)
plt.xlabel('Number of Vertices')
plt.ylabel("Execution time to find MinHam cycle (in ms)")
plt.title("Exec time vs vertices Graph", fontsize = '20', color = 'g')
plt.legend(["Naive", "Approx_Algo"])
plt.show()