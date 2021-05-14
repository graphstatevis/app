def Adj2GraphID(adj):
    n = adj.shape[0]
    GraphID = str(n)+"_"
    binID = ''
    for i in range(n):
        for j in range(i+1,n): 
            binID += str(int(adj[i][j]))
    GraphID += hex(int(binID,2)).split('x')[1]
    return GraphID.upper()


def GraphID2Adj(GraphID):
    n_str, hexID = GraphID.split("_")
    n = int(n_str)
    binID = "{:b}".format(int(hexID, 16)) 
    binID = '0'*((n-1)*n//2 - len(binID)) + binID  
    adj = np.zeros([n,n])
    pos = 0
    for i in range(n):
        for j in range(i+1,n): 
            adj[i][j] = adj[j][i] = int(binID[pos])
            pos +=1 
    return adj
