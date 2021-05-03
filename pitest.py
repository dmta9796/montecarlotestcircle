import matplotlib.pyplot as plt
import numpy as np
import random

def makepoint():
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    return np.array([[x,y]])

def dist(p1):
    distance = np.linalg.norm(p1, ord=2)
    return distance

if __name__ == "__main__":
    limit = 1000000
    num = 0
    dem = 0
    points = np.empty((0,2))
    #print(points[:,0],points[:,1])

    for number in range(limit):
        point = makepoint()
        #print(point.shape,point.shape)
        points = np.append(points,point, axis = 0)
        #print(point)
        dem += 1
        #print("test:",num,":",dist(point)<0.0)
        distance = dist(point)
        if(distance<1.0):
            num += 1
        #plt.scatter(points[:,0],points[:,1])
        #plt.xlim(0,1)
        #plt.ylim(0,1)
        #plt.draw()
        #print(num,dem,4*(num/dem))
        #plt.show(block=False)
        #input("Press Enter to continue...")
    print(num,dem,4*(num/dem))