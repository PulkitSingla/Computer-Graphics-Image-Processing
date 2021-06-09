from tsp_solver.greedy import solve_tsp
def tsp(dist,obj):
    path=[]
    for i in dist:       
        path.append(solve_tsp(i))
    pt=[]
    for i in range(len(path)):
        temp=[]
        for j in range(len(path[i])):
            k=path[i][j]
            t=list(obj[i][k])
            temp.append((t[0],t[1]))
        pt.append(temp)
    path=pt.copy()
    return path