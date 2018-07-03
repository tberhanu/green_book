#We can use this function to get the FIRST COMMON ANCESTOR btn two nodes, 
# by calling path_between(head, node1) and path_between(head, node2), and
# then by comparing the resulted stacks which isn't time efficient
def path_between(head, node):
	# Use STACK to collect the path starting all the way DOWN to UP

	if head == None:
		s = Stack()
		return s
	if head == node:
		s = Stack
		s.push(head)
		return s

	left_stack = path_between(head.left, node)
	right_stack = path_between(head.right, node)

	# Remember there is no way that both left_stack and right_stack would return
	# non empty stack. Only one of them can be non empty or both will be empty

	#Therefore, we return only the non empty stack if there is 

	if len(left_stack) != 0:
		added_stack = left_stack.push(head)
		return added_stack
	else if len(right_stack != 0):
		added_stack = right_stack.push(head)
		return added_stack
	else:
		return s #this is empty stack

def least_common_ancestor(head, node1, node2):

	if node1 == node2: 
		return node1
	path1 = path_between(head, node1)
	path2 = path_between(head, node2)

	if len(path1) == 0 or len(path2) == 0:
		return None

	prev = None
	while !path1.isEmpty() and !path2.isEmpty():
		n1 = path1.pop()
		n2 = path2.pop()
		if n1 == n2:
			prev = n1
		else:
			return prev
			













