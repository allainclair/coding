def shortest_path(adjs, current_vertex):
	visited = set(current_vertex)
	paths = [float("inf") for _ in adjs]
	paths[current_vertex] = float("inf")

	while len(visited) < len(adjs):
		min_path = paths[current_vertex]
		for adj in adjs[current_vertex]:
			if adj[1] < min_path:
				min_adj = adj


def main():
	adjs = [  # (adj, w)
		{(1, 2), (2, 6)},  # v 0
		{(0, 2), (3, 5)},  # v 1
		{(0, 6), (3, 8)},  # v 2
		{(1, 5), (2, 8), (5, 15), (4, 10)},  # v 3
		{(3, 10), (5, 6), (6, 2)},  # v 4
		{(3, 15), (4, 6), (6, 6)},  # v 5
		{(4, 2), (5, 6)},  # v 6
	]
	shortest_path(adjs, 0)


if __name__ == "__main__":
	main()
