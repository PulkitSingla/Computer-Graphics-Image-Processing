import matplotlib.pyplot as plt
import math
def dft(x):
  X = [];
  N = len(x);
  for k in range(N):
    re = 0;
    im = 0;
    for n in range(N):
      phi = (2*math.pi * k * n) / N;
      re += x[n] * math.cos(phi);
      im -= x[n] * math.sin(phi);
    re = re / N;
    im = im / N;
    freq = k;
    amp = (re * re + im * im)**0.5;
    phase = math.atan2(im, re);
    X.append([ re, im, freq, amp, phase ]);
  return X;


def epiCycles(x, y, rotation, fourier,time):
  for i in range(len(fourier)):
    freq = fourier[i][2]
    radius = fourier[i][3]
    phase = fourier[i][4]
    x += radius * math.cos(freq * time + phase + rotation);
    y += radius * math.sin(freq * time + phase + rotation);
  return [x, y]

def dft_2d(T):
    a=1
    x=[]
    y=[]
    for i in T:
        x.append(i[0])
        y.append(i[1])
    Y=dft(y)
    X=dft(x)
    x2=[]
    y2=[]
    t=0
    dt=(2*math.pi)/(len(X)*a)
    for i in range(a*len(x)):
        vx = epiCycles(0, 0, 0, X,t);
        vy = epiCycles(0, 0, math.pi/2,Y,t);
        t=t+dt
        x2.append(vx[0])
        y2.append(vy[1])
        
    plt.scatter(y2,x2,s=4)
    plt.gca().invert_yaxis()
    plt.show