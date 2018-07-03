def has_route(node1, node2):
	# Use BFS, preffered way 
	visited_set = ()
	q = Queue()
	q.push(node1)
	while !q.isEmpty()
		top = q.pop()
		if top == node2:
			return True
		visited_set.add(top)
		for node in top.adjacencies:
			if node not in visited_set:
				q.enqueue(node)
	return False
###########################################################
def has_route2(node1, node2):
	# Use DFS
	visited_set = ()
	return dfs(node1, node2, visited_set)
def dfs(node1, node2, visited_set):
	if node1 == node2:
		return True
	visited_set.add(node1)
	for node in node1.adjacencies:
		if node not in visited_set:
			dfs(node1, node2, visited_set) 


#########################################
#Here is how to get the shortest route using BFS

def shortest_path(node1, node2):
	visited = ()
	q = Queue()
	q.enqueue(node1)
	shortest = {node1, [node2]}
	while !q.isEmpty():
		node = q.dequeue
		visited.add(node)
		for adj in node.adjs:
			shortest[adj] = shortest[node] + adj
			if adj == node2:
				return shortest[adj]
			q.enqueue(adj)
	return None






















