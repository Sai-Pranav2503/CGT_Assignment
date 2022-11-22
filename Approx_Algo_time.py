import random
import time
import matplotlib.pyplot as plt

input_l = []
ApproxAlgo_l = []

for V in range(1,200):
  input_l.append(V)
  l=[]
  for i in range(V):
      l1 = []
      for j in range(V):
          if i == j:
              l1.append(0)
          else :
              l1.append(1)
      l.append(l1)

  a = random.randint(3, 30)
  w = l

  for i in range(V):
    for j in range(i,V):
      if i != j:
        w[i][j]=random.randint(a, 2*a -1)
        w[j][i]=w[i][j]

  G = []
  graph = []
  for i in range(V):
      l=[]
      for j in range(V):
          if w[i][j]!=0:
              l.append(1)
              G.append([i,j,w[i][j]])
          else:
              l.append(0)
      graph.append(l)
  
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
plt.plot(input_l, ApproxAlgo_l)
plt.xlabel('Number of Vertices')
plt.ylabel("Execution time for TSP with Approx Algo (in ms)")
plt.title("Exec time vs vertices Graph", fontsize = '20', color = 'g')
plt.show()