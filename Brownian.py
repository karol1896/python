from scipy import linalg
import numpy as np
import matplotlib.pyplot as pyplot

N = 100
Delta = 0.1
Sigma = 0.1
Mu = 0.04
Size = 5
P = 0.9
Cor = np.full((size, size), p)
for i in range(size):
    Cor[i, i] = 1

L = linalg.cholesky(Cor, lower = True)

sample = np.random.normal(loc=0, scale=np.sqrt(delta)*sigma, size = (n, size , 1))

for k in range(n):
    sample[k] = L @ sample[k]
sample[0] = np.full((5,1), 0)
for k in range(1,n):
    for i in range(size):
        dw = mu * delta + sample[k][i][0]
        sample[k][i][0] = dw + sample[k-1][i][0]

t = np.arange(0.0, n*delta, delta)
s = np.zeros((size, N))
plt.figure(figsize = (18,10))
for k in range(size):
    s[k] = sample[:, k, 0]
    plt.plot(t, s[k])

plt.show()