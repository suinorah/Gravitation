import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
fig, ax = plt.subplots()
G=1
N = 3

def distance (X,Y):
    a,b = X
    c,d = Y
    return np.sqrt ( (a-c)**2 + (b-d)**2 )

ax.axis('equal')
#ax.set(xlim=[-1, 1000], ylim=[-1,1000])


positions = np.random.randint(0,1001,2*N).reshape(N,2)
vitesses = np.zeros(2*N).reshape(N,2)
masses= np.random.randint(1,5,N)
"""vecteurs = np.zeros((N,N,2))
for i in range (N):
    for j in range (N):
        if i!=j : 
            Pi = positions [i]
            Pj =positions [j]
            vecteurs[i][j] = (Pj - Pi)/distance(Pi,Pj)"""

vecteurs = positions[:,np.newaxis,:] - positions[np.newaxis,:,:]
distances = np.sqrt((vecteurs*vecteurs).sum(axis=2))



"""def get_new_position(position):
    a = 

def get_new_acc (acc) :
    

scat = ax.scatter(positions[0], positions[1])

def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global positions
    positions = get_new_position(positions)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(positions).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100)
plt.show()"""