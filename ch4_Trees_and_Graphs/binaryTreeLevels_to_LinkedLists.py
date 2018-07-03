# Able to get a dict of node_level = {head:0, left1:1, right1:1, left2:2, right2:2, 
# left2.1:2, right2.2:2, .....} , but need also make llist based on their level 
# which needs to be done next time
def binaryTreeLevels_to_LinkedLists(tree):
	#we use a concept of DFS
	visited = ()
	q = Queue()
	head = tree.data
	node_level = {}
	level_node = {}
	node_level[head] = 0 # dist = {node:0, .....}
	level_nodes[0] = [head]
	q.enqueue(head)
	while !q.isEmpty():
		node = q.dequeue()
		# visited.add(node)
		for child in node.children:
			node_level[child] = node_level[node] + 1
			q.enqueue(child)
