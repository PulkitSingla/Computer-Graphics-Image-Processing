from matplotlib import pyplot as plt
def gray(img):
    plt.imshow(img,cmap = 'gray')
    plt.show()
def mult(obj,pt_size, line_size):
    for j in range(len(obj)):
        x1=[]
        y1=[]
        for i in range(len(obj[j])):
            t=list(obj[j][i])
            x1.append(t[0])
            y1.append(t[1])
        plt.plot(y1,x1,'black', marker='D',linewidth=line_size,markersize=pt_size,linestyle='--')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()
    plt.show()
