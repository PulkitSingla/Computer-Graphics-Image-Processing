import cv2
import find_objects as fo
import plot 
import distance_matrix as dm
import shortest_path as sp
import Fourier_Series as fs
import numpy as np
"""import Fourier as fr"""

#Read file and initial conditions
img = cv2.imread('C:/Users/Kanishk/Desktop/Project/CGProject/New/o.jpg')
a=4
save_path='C:/Users/Kanishk/Desktop/o_path.png'
#convert into line drawing
plot.gray(img)
edges = cv2.Canny(img,100,250)
plot.gray(edges)
#reducing no of points
obj=fo.reduce(img,edges,a)
if len(obj)<2:
    obj.append([(0,0)])
#plotting obj
plot.mult(obj,0.5,0)
#solving using tsp-greedy
dist=dm.create(obj)
#making path matrix  
path=sp.tsp(dist,obj)
ma=0;
for i in range(len(path)):
    if ma< np.amax(path[i]):
        ma=np.amax(path[i])
for i in range(len(path)):
    for j in range(len(path[i])):
        x=int(path[i][j][0]/ma*400)
        y=int(path[i][j][1]/ma*400)
        path[i][j]=(x,y)
        
plot.mult(path,0,0.2)
for i in path:
    fs.dft_2d(i)
path=np.array(path)
path=path.reshape(path.shape[0],-1)
np.savetxt("./GlutMain/GlutMain/file.txt",path,fmt='%5s')