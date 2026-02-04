graph={
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],    
    '5': ['7'],
    '6': [],
	'7':[]
}
visited = []
queue = []
def bfs(visited, graph, node):
	visited.append(node)
	queue.append(node)
	while queue:
		s=queue.pop(0)
		print(s,end=" ")
		for neighbour in graph[s]:
			visited.append(neighbour)
			queue.append(neighbour)
bfs(visited,graph,'1')