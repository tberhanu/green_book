def return_kth_to_last(llist, k):
	
	current, follower = llist, llist
	for i in range(k):
		current = current.next
	while current != None:
		current = current.next
		follower = follower.next
	return follower
class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

head = Node(1, Node(2, Node(2, Node(5, Node(1, Node(5, Node(2, None)))))))
head2 = return_kth_to_last(head, 4)
while head2:
	print(head2.data)
	head2 = head2.next
print("Another test")
head = Node(1, Node(2, Node(2, Node(5, Node(1, Node(5, Node(2, None)))))))
head2 = return_kth_to_last(head, 2)
while head2:
	print(head2.data)
	head2 = head2.next
print("Another test")
head = Node(1, Node(2, Node(2, Node(5, Node(1, Node(5, Node(2, None)))))))
head2 = return_kth_to_last(head, 6)
while head2:
	print(head2.data)
	head2 = head2.next