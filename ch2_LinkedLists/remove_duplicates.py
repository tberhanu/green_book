
class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

def remove_duplicates(llist):
	node = llist 
	if node:
		values = set([node.data])
		while node.next:
			if node.next.data not in values:
				values.add(node.next.data)
				node = node.next
			else:
				node.next = node.next.next
		return llist

head = Node(1, Node(2, Node(2, Node(5, Node(1, Node(5, Node(2, None)))))))
head2 = remove_duplicates(head)
while head2:
	print(head2.data)
	head2 = head2.next
print("another test")
head = Node(8, Node(2, Node(9, Node(2, None))))
head2 = remove_duplicates(head)
while head2:
	print(head2.data)
	head2 = head2.next

