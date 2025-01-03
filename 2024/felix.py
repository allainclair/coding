"""
Origin: 0
Destination: 8
Number of vertices: 9
Edges weights: [0, 1, 0.25], [0, 2, 0.3], [1, 3, 0.3], [1, 4, 0.15], [2, 4, 0.20], [2, 5, 0.20], [3, 6,
0.1], [3,7, 0.15], [4, 7, 0.2], [5, 7, 0.30], [6, 8, 0.3], [7, 8, 0.15]
"""
import heapq


def create_adjs(n_vertices, edges_weights):
	adjs = [set() for _ in range(n_vertices)]
	for edge_weight in edges_weights:
		origin_vertex, dest_vertex, weight = edge_weight
		adjs[origin_vertex].add((dest_vertex, weight))
	return adjs


def minimum_cost(origin, destination, n_vertices, edges_weights):
	adjs = create_adjs(n_vertices, edges_weights)
	# print(adjs)

	# visited_nodes = set()

	cost_paths = [float("inf")]*n_vertices
	queue = []
	heapq.heappush(queue, (0, origin))  # cost, vertex

	cost_paths[0] = 0
	while queue:
		current_weight, current_vertex = queue.pop()

		for adj in adjs[current_vertex]:
			dest, weight = adj
			if cost_paths[dest] > current_weight + weight:
				cost_paths[dest] = current_weight + weight

			heapq.heappush(queue, (dest, weight))

	min_cost = cost_paths[destination]  # last vertex
	return min_cost


def main():
	origin = 0
	destination = 8
	n_vertices = 9
	edges_weights = [
		[0, 1, 0.25],
		[0, 2, 0.3],
		[1, 3, 0.3],
		[1, 4, 0.15],
		[2, 4, 0.20],
		[2, 5, 0.20],
		[3, 6, 0.1],
		[3,7, 0.15],
		[4, 7, 0.2],
		[5, 7, 0.30],
		[6, 8, 0.3],
		[7, 8, 0.15],
	]
	min_cost = minimum_cost(origin, destination, n_vertices, edges_weights)
	pass


if __name__ == "__main__":
	main()
