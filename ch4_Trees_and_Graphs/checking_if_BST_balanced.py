import Math
def checking_if_BST_balanced(node):
	""" Basically if the tree is balanced, then for every arbitrary NODE, 
	the d/ce b/n the MAXIMUM HEIGHT of the LEFT and RIGHT branches should be
	less than or equal to ONE. https://www.youtube.com/watch?v=TWDigbwxuB4 """ 
	# so, this function will return -1 if the tree is not balanced, otherwise
	# it will return the HEIGHT OF THE TREE

	if node == None: # this also handles the LEAF NODE cases whose LEFT and RIGHT
		return 0      # nodes are NONE

	left_height = checking_if_BST_balanced(node.left)
	right_height = checking_if_BST_balanced(node.right)

	if Math.abs(left_height - right_height) > 1:
		return -1 # this means that it is not balanced
	if left_height == -1:
		return -1
	if right_height == -1:
		return -1

	return 1 + Math.max(left_height, right_height)

class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.parent = None
		if self.left:
			self.left.parent = self
		if self.right:
			self.right.parent = self
			