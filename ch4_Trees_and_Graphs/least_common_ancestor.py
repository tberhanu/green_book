def least_common_ancestor(head, node1, node2):

	if head == None:
		return None
	if head == node1 or head == node2:
		return head
	
	left = least_common_ancestor(head.left, node1, node2)
	right = least_common_ancestor(head.right, node1, node2)

	if left and right:
		return head
	
	if left == None and right == None:
		return None
	# if left == None and right != None:
	# 	return right
	# if right == None and left != None:
	# 	return left
	return left if left else right


