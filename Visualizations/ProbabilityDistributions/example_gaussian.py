# Adapted from example at https://matplotlib.org/stable/plot_types/basic/plot.html
# Plotting Gaussian pdfs from https://www.math.net/gaussian-distribution

import matplotlib.pyplot as plt
import numpy as np
from Visualizations.ProbabilityDistributions.gaussian import gaussian_pdf

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(-8, 16, 200)

mu1 = 0
sigma1 = 1
y1 = np.array(list(map(lambda var: gaussian_pdf(mu1, sigma1, var), x)))

mu2 = 4
sigma2 = 3
y2 = np.array(list(map(lambda var: gaussian_pdf(mu2, sigma2, var), x)))

mu3 = 10
sigma3 = 2
y3 = np.array(list(map(lambda var: gaussian_pdf(mu3, sigma3, var), x)))

# plot
plt.plot(x, y1, 'r', linewidth=2.0, label=f'mu={mu1}, sigma={sigma1}')
plt.plot(x, y2, 'b', linewidth=2.0, label=f'mu={mu2}, sigma={sigma2}')
plt.plot(x, y3, 'g', linewidth=2.0, label=f'mu={mu3}, sigma={sigma3}')
plt.legend()
plt.show()
