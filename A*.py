import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from random import choice

plt.figure(figsize=(10, 10))
N = 10
M = 20
obstacles = 40

G = nx.grid_2d_graph(N, M)
edges_to_delete = np.random.randint(0, N, size=(obstacles, 2))
edges_to_delete = list(map(tuple, edges_to_delete))
G.remove_nodes_from(edges_to_delete)

pos = dict((n, n) for n in G.nodes())
labels = dict(((i, j), i * 10 + j) for i, j in G.nodes())



for i in range(5):
	nx.draw_networkx(G, pos=pos, labels=labels)
	points = (choice(list(pos.values())), choice(list(pos.values())))
	try:
		path = nx.algorithms.shortest_paths.astar.astar_path(G, *points)
	except Exception:
		print("There is no way between {0} and {1} vertices on {3} iteration.".format(str(points[0]), str(points[1]), i + 1))

	print(points)
	print(path)

	nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='r')
	plt.draw()
	plt.show()
	plt.clf()