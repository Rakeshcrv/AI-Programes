graph={
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],    
    '5': ['7'],
    '6': [],
    '7':[]
}
visited=set()
def dfs(visited,graph,node):
	if node not in visited:
		print(node)
	visited.add(node)
	for neighbour in graph[node]:
		dfs(visited,graph,neighbour)
dfs(visited,graph,'1')