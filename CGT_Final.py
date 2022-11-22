import networkx as nx
import matplotlib.pyplot as plt

class Graph_plot:
    
    def __init__(self):
        self.edgelist=[]        

    def addEdge(self,a,b,wt):
        t=[a,b,wt]
        self.edgelist.append(t)

    def plot(self):
        G = nx.Graph()
        for i in self.edgelist:
            G.add_edge(i[0],i[1],weight=i[2])
        pos=nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=150, node_color = "#7b9953")
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_size=11, font_family="sans-serif", font_color="k")
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G,pos,edge_labels,font_size=10)
        plt.show()

import random

V = int(input("Enter the number of vertices: "))
print("\nAdjacency Matrix of K{}: ".format(V))
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
      w[i][j]=random.randint(a, 2*a -5)
      w[j][i]=w[i][j]
for l in w:
  print(l)

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
print("\nGraph: ")
gp = Graph_plot()
for i in range(len(G)):
    gp.addEdge(G[i][0],G[i][1],G[i][2])
gp.plot()
print("\n---------------------------------------------\n")

#Prim
prim_mst=[]
def Prim(G, v):
    Infinity = 9999999
    chosen = [0]*v
    no_edge = 0
    chosen[0] = True
    print("MST using Prim's Algo: \n")
    print("Edge: Weight")
    while (no_edge < v - 1):
        min = Infinity
        x = 0
        y = 0
        for i in range(v):
            if  chosen[i]:
                for j in range(v):
                    if ((not chosen[j]) and G[i][j]):  
                        if min > G[i][j]:
                            min = G[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ": " + str(G[x][y]))
        prim_mst.append([str(x), str(y), str(G[x][y])])
        chosen[y] = True
        no_edge += 1

Prim(w, V)
print("\n")
MST1 = Graph_plot()
for i in range(len(prim_mst)):
    MST1.addEdge(prim_mst[i][0],prim_mst[i][1],prim_mst[i][2])
MST1.plot()
print("\n---------------------------------------------\n")

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
        print("MST using Kruskal's Algo: \n")
        print("Edge: Weight")
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
            print("%d-%d: %d" % (u, v1, weight))
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
print("\nMinimal spanning tree cost:", tree_size, '\n')

MST2 = Graph_plot()
for i in range(len(kruskal_mst)):
    MST2.addEdge(kruskal_mst[i][0],kruskal_mst[i][1],kruskal_mst[i][2])
MST2.plot()
print("\n---------------------------------------------\n")

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

    print("Minimum Hamiltonian cycle using Approx Algo:")
    cost=0
    for i in range(V-1) :
        cost+=w[l[i]-1][l[i+1]-1]
        print(l[i]-1,"->",end=" ")
        Ham_l.append([l[i]-1, l[i+1]-1, w[l[i]-1][l[i+1]-1]])
    
    cost+=w[l[V-1]-1][0]
    print(l[V-1]-1,"->",l[0]-1)
    Ham_l.append([l[V-1]-1, l[0]-1, w[l[V-1]-1][l[0]-1]])
    print("Length of minimum Hamiltonian cycle:", cost)

MinHam_ApproxAlgo()
print("\n")
Ham = Graph_plot()
for i in range(len(Ham_l)):
  Ham.addEdge(Ham_l[i][0], Ham_l[i][1], Ham_l[i][2])
Ham.plot()