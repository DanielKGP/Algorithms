G = {1:{1:0, 2:-3, 5:5},
      2:{2:0, 3:2},
      3:{3:0, 4:3},
      4:{4:0, 5:2},
      5:{5:0}}

def getEdges(G):
     v1 = []
     v2 = []
     w  = []
     for i in G:
         for j in G[i]:
             if G[i][j] != 0:
                 w.append(G[i][j])
                 v1.append(i)
                 v2.append(j)
     return v1,v2,w

def Bellman_Ford(G, v0, INF=999):
     v1,v2,w = getEdges(G)

     dis = dict((k,INF) for k in G.keys())
     dis[v0] = 0

     for k in range(len(G)-1):
         check = 0
         for i in range(len(w)):
             if dis[v1[i]] + w[i] < dis[v2[i]]:
                 dis[v2[i]] = dis[v1[i]] + w[i]
                 check = 1
         if check == 0: break

     flag = 0
     for i in range(len(w)):
        if dis[v1[i]] + w[i] < dis[v2[i]]:
             flag = 1
             break
     if flag == 1:
        return False
     return dis

v0 = 1
dis = Bellman_Ford(G, v0)
print dis.values()
