import numpy as np


n =  int(input("n-dim vector: "))
vls = []
for i in range(n):
    v = [int(x) for x in input("Enter vector elements separated by space: ").split()]
    vls.append(np.array(v, dtype=float))

uls = [0 for _ in range(n)]
grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(0,n):
    vi = vls[i]
    ui = vi.copy()
    for j in range(i):
        uj = uls[j]
        muji = np.dot(vi,uj)/(np.linalg.norm(uj) ** 2)
        ui = ui - np.dot(muji, uj)
    uls[i] = ui

print(uls)

