def is_subtree(tree, subtree):
	if subtree == None:
		return True
	if tree == None:
		return False
	if is_identical(tree, subtree):
		return True
	return is_subtree(tree.left, subtree) or is_subtree(tree.right, subtree)

def is_identical(tree1, tree2):
	if tree1 == None and tree2 == None:
		return True
	if tree1.data != tree2.data:
		return False
	if tree1 != None and tree2 != None:
		return is_identical(tree1.left, tree2.left) and is_identical(tree1.right, tree1.right)
	return False