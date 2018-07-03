def get_BST_node_successor(node):
	""" We first step to the RIGHT and then all the way to
	 the LEFT to get SUCCESSOR"""
	 # I think this code is enough as dealing with BST make things easier
	if node == None:
		return None

	child = node.right
	if child:
		while child.left:
			child = child.left
	return child

class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.parent = None
		if self.left:
			self.left.parent = self
		if self.right:
			self.right.parent = self
			