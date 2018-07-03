## AMAZING REAL LIFE APPLICATION OF THE GRAPH AND QUEUE

def build_project_order(projects, dependencies):
	"""projects: [A, B, C, D]
	dependencies: [(A, C), (A, D)]"""
	"""We need to construct a DAG, so we define the NODE of the GRAPH 
	as PROJECTS, and the DIRECTED EDGE as a sign of dependency of one
	project on the other. Therefore, when adding an EDGE from A to C, 
	we need also to increment A's number of dependencies by one"""

	#Lets construct a GRAPH via the given parameters
	nodes = {} # Dictionary: {project1:node1, proj2:node2, .....}
	for project in projects:
		node = NodeGraph(project)
		nodes[project] = node
	for dependent in dependencies:
		# dependent_project --> arrow_project: tail_proj depends on arrow_proj
		dependent_project = nodes[dependent[0]]
		arrow_project = nodes[dependent[1]]
		dependent_project.add_edge(arrow_project)
	q = Queue()
	build_order = []
	for project in projects:
		if project.dependencies == 0:
			q.enqueue(project.data)

	while !q.isEmpty():
		node = q.dequeue
		build_order.append(node)
		for dependent in node.edges:
			dependent.dependencies -= 1
			if dependent.dependencies == 0:
				q.enqueue(dependent)

	if len(build_order) < len(projects):
		return Exception("Dependency Cycle Detected")
	return build_order

class NodeGraph():
	def __init__(self, data):
		self.data = data
		self.dependencies = 0
		self.edges = []
	def add_edge(self, node):
		self.edges.append(node)
		self.dependencies += 1

class Queue():
	def __init__(self):
		self.array = []

	def remove(self):
		return self.array.pop(0)
	def add(self, item):
		self.array.append(item)
	def isEmpty(self):
		return len(self.array) == 0



