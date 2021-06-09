def create(obj):
    megadist=[]
    dist=[]
    for i in obj:
        for j in range(len(i)):
            t=[]
            for k in range(len(i)):
                t1=((i[j][0]-i[k][0])**2+(i[j][1]-i[k][1])**2)**0.5
                t.append(t1)
            dist.append(t)
        megadist.append(dist)
        dist=[]
    return megadist
