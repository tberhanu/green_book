
# this code is done exclusively by me, Tess
def paths_with_sum(tree, sum, cntr):
	if tree == None:
		return 0
	if tree.left == None and tree.right == None:
		if sum - tree.data == 0:
			cntr += 1
			return cntr
		else:
			return 0
	left = paths_with_sum(tree.left, sum - tree.data, cntr)
	right = paths_with_sum(tree.right, sum - tree.data, cntr)
	if sum - tree.data == 0:
		return left + right + 1
	else:
		return left + right
def complete_generalizer(tree, sum, cntr):
	return paths_with_sum(tree, sum, cntr) + generalizer(tree, sum, cntr)
def generalizer(tree, sum, cntr):
	if tree == None:
		return 0
	left = paths_with_sum(tree.left, sum, cntr)
	right = paths_with_sum(tree.right, sum, cntr)
	if left != None and right != None:
		return left + right + generalizer(tree.left, sum, left) + generalizer(tree.right, sum, right)
	return left + right

class Node():
	def __init__(self, data, name="", left=None, right=None):
		self.data = data
		self.name = name
		self.left = left
		self.right = right
k = Node(3, "K")
a = Node(5, "a", k, None)
b = Node(4, "b")
c = Node(1, "c", None, b)
d = Node(4, "d", a, c)
e = Node(7, "e")
f = Node(9, "f")
g = Node(3, "g", e, f)
h = Node(8, "h", d, g)
print("here is starting at ROOT and ending anywhere")
print(paths_with_sum(h, 12, 0)) 
print(paths_with_sum(h, 9, 0))
print("here is starting anywhere and ending anywhere")
print(complete_generalizer(h, 12, 0)) 
print(complete_generalizer(h, 9, 0))




