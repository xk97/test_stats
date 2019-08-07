#%% Monty Hall problem
import numpy as np

n_trails, n_doors = 1000, 3

idx_X = np.random.choice(range(n_doors), n_trails)
X = np.zeros((n_trails, n_doors))
for i in range(n_trails):
    X[i, idx_X[i]] = 1
print(X)
#%% no change in choice
y = np.random.choice(range(n_doors), n_trails)
print(f'corrected ratio: {np.sum(y==idx_X) / n_trails}')
#%% change choice after k round

