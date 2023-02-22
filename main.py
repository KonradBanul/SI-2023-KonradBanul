import numpy as np

data = np.loadtxt("australian.txt", dtype=str)

i = 0
for row in data:
    i += 1

min_val = data.min(axis=0)
print(i)