# from LinkedList import LinkedList
def check_llist_palindrome(llist):
	curr = llist
	runner = llist
	stack = [] #In python we use 'lists' as 'stacks'
	while runner and runner.next:
		stack.append(curr.data)
		curr = curr.next
		runner = runner.next.next
	if runner:
		curr = curr.next
	while curr:
		top = stack.pop()
		if top != curr.data:
			return False
		curr = curr.next
	return True

class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

ll1 = Node(1, Node(2, Node(3, Node(2, Node(1, None)))))
print(check_llist_palindrome(ll1))
ll2 = Node(1, Node(2, Node(3, Node(3, Node(2, Node(1, None))))))
print(check_llist_palindrome(ll2))
ll3 = Node(1, Node(2, Node(3, Node(2, Node(2, Node(1, None))))))
print(check_llist_palindrome(ll3))