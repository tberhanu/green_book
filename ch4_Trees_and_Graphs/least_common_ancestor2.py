def least_common_ancestor2(node1, node2):
	if node1 == node2:
		return node1
	ancestor1 = set()
	ancestor2 = set()
	while node1.parent or node2.parent:

		if node1 and node1.parent in ancestor2:
			return node1.parent
		if node1 and node1.parent not in ancestor2:
			ancestor1.add(node1)
			node1 = node1.parent

		if node2 and node2.parent in ancestor1:
			return node2.parent
		if node2 and node2.parent not in ancestor1:
			ancestor2.add(node2)
			node2 = node2.parent

	return None
	
class TreeNode():
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right
		self.parent = None
