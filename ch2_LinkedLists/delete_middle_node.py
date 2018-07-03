#Watch out, its a little bit tricky
def delete_middle_node(node):
  	node.data = node.next.data
  	node.next = node.next.next
  	# return node


class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

head = Node(1, Node(2, Node(333, Node(5, Node(1, Node(5, Node(2, None)))))))

delete_middle_node(head.next.next)
while head:
	print(head.data)
	head = head.next
