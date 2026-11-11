import numpy as np

u = np.array([int(x) for x in input("Enter 2 dim vector elements separated by space: ").split()])
v = np.array([int(x) for x in input("Enter 2 dim vector elements separated by space: ").split()])
temp = np.array([])

def glr(v1,v2):
    while True:
        if np.linalg.norm(v2) < np.linalg.norm(v1):
            temp = v1.copy()
            v1 = v2.copy()
            v2 = temp.copy()
        m = round(np.dot(v1,v2)/np.dot(v1,v1))
        if m == 0:
            break
        v2 = v2-np.dot(m,v1)
    return v1,v2

u,v = glr(u,v)
