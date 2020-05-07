import numpy as np
from copy import deepcopy

n = 100
out_data = deepcopy(in_data)
out_data.X[out_data.X < n] = 0
ar = np.argwhere(out_data.X)

cols, shifts = np.unique(ar[:, 1], return_counts=True)
out_data.X = np.array([np.roll(out_data.X[:, col], shift) for col, shift in zip(cols, shifts)]).T
out_data.X[out_data.X==0]= np.nan