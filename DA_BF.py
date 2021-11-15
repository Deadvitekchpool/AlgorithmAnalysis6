import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from random import choice

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from random import choice

def measure_time(n_experiments, method, g, source, dest):
    times = []
    for i in range(10):
        start_time = timer()
        method(g, source, dest, 'weight')
        times.append(timer() - start_time)
    
    return np.array(times, dtype=np.float64).mean(axis=0)

n = 100
m = 500

g = nx.gnm_random_graph(n, m)
weights = np.random.randint(100, size=m)

weights_matrix = np.zeros((m, m))

for i, elem in enumerate(g.edges()):
    g[elem[0]][elem[1]]['weight'] = weights[i]
    g[elem[1]][elem[0]]['weight'] = weights[i]

nx.draw(g)
plt.draw()
plt.show()

print('DA: {:.6f}'.format(measure_time(10, nx.algorithms.shortest_paths.weighted.dijkstra_path, g, np.random.randint(0, 99), np.random.randint(0, 99))))
print('BFA: {:.6f}'.format(measure_time(10, nx.algorithms.shortest_paths.weighted.bellman_ford_path, g, np.random.randint(0, 99), np.random.randint(0, 99))))