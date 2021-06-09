import numpy as np

def reduce(img,edges,a):
    img_b=len(img)
    img_h=len(img[0])
    edges2=np.copy(edges)
    while True:
        ans = np.empty(shape=(img_b,img_h))
        ans.fill(255)
        coord=[]
        b=int((a-1)/2)+1
        for i in range(b,img_b,a):
            for j in range(b,img_h,a):
                x=0
                xc=0
                y=0
                yc=0
                for m in range(a):
                    for l in range (a):
                        if(i+m-b<img_b and j+l-b<img_h):
                            if(edges2[i+m-b,l+j-b]==255):
                                x=x+m-b
                                y=y+l-b
                                xc=xc+1
                                yc=yc+1
                if xc>0 or yc>0:
                    x=int((x+0.5)/xc)
                    y=int((y+0.5)/yc)              
                    ans[i+x,j+y]=0
                    coord.append((i+x,j+y))
        #no of objects
        obj=[]
        objt=[]
        qu=[]
        coordt=coord.copy()
        while len(coordt)!=0:
            qu.append(coordt[0])
            coordt.pop(0)
            while len(qu)!=0:
                t=qu[0]
                coordt2=coordt.copy()
                for i in coordt:
                    if i[0]>t[0]-a-1 and i[0]<t[0]+a+1 and i[1]>t[1]-a-1 and i[1]<t[1]+a+1:
                        qu.append(i)
                        coordt2.remove(i)
                objt.append(qu[0])
                qu.pop(0)
                coordt=coordt2.copy()
            obj.append(objt)
            objt=[]
        flag=0;
        for i in obj:
            if len(i)>2000:
                flag=1
        if flag==0:
            break
        else:
            a=a+1
    tobj=obj.copy()
    for i in obj:
        if len(i)<=20:
            tobj.remove(i)
    obj=tobj.copy()
    return obj