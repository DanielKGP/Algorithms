
import sys

G = {1:{1:0,    2:2,    3:6,    4:4},
     2:{1:sys.maxint,  2:0,    3:3,    4:sys.maxint},
     3:{1:7,    2:sys.maxint,  3:0,    4:1},
     4:{1:5,    2:sys.maxint,  3:12,   4:0}}


for k in G.keys():
     for i in G.keys():
         for j in G[i].keys():
             if G[i][j] > G[i][k] + G[k][j]:
                 G[i][j] = G[i][k] + G[k][j]


for i in G.keys():
     print G[i].values()
