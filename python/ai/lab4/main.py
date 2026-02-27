import numpy as np

data = np.random.rand(24 * 60, 12)
data = data.reshape(14, 60, 12)
print(data)

