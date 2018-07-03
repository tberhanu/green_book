def sorted_array_to_BSTree(sorted_array):
	
	mid = (start + end) /2
	data = array[mid]
	left = sorted_array_to_BSTree(array[:mid - 1])
	right = sorted_array_to_BSTree(array[mid + 1:])
	bst_tree = BSTNode(data, left, right)
	return bst_tree

class BSTNode():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = None
		if self.left:
			self.left.parent = self
		if self.right:
			self.right.parent = self
