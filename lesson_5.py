"""
https://realpython.com/lessons/kernel-density-estimates/
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

means = 10, 20
stdevs = 4, 2

dist = pd.DataFrame(
    np.random.normal(loc=means, scale=stdevs, size=(1000, 2)),
    columns=['a', 'b']
)

fig, ax = plt.subplots()
dist.plot.kde(ax=ax, legend=False, title='Histogram: A vs. B')
dist.plot.hist(density=True, ax=ax)
ax.set_ylabel('Probability')
ax.grid(axis='y')
ax.set_facecolor('#d8dcd6')

plt.show()
