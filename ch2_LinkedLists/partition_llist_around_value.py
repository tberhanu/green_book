#Hard Qn: Not yet solved
import copy
def partition_llist_around_value(x, llist):
	"All 'llist' elements less than 'x' to the LEFT, and the rest to the RIGHT"

	left_llist = get_left_llist(x, llist)
	right_llist = get_right_llist(x, llist)
	while left_llist:
		left_llist = left_llist.next

	left_llist.next = right_llist
	return left_llist

def get_left_llist(x, llist):
	ptr1 = copy.deepcopy(llist) #for those less than 'x'
	while ptr1:
		if ptr1.data < x:
			ptr1 = ptr1.next

		else:
			if ptr1.next:
				ptr1.data = ptr1.next.data
				ptr1.next = ptr1.next.next 
			else:
				ptr1 = ptr1.next
	return ptr1

def get_right_llist(x, llist):
	ptr2 = copy.deepcopy(llist) #for those greater than 'y'
	while ptr2:
		if ptr2.data >= x:
			ptr2 = ptr2.next
		else:
			if ptr2.next:
				ptr2.data = ptr2.next.data
				ptr2.next = ptr2.next.next 
			else:
				ptr2 = ptr2.next
	return ptr2

class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
resulted_llist = partition_llist_around_value(6, head1)
while resulted_llist:
	print(resulted_llist.data)
	resulted_llist = resulted_llist.next

















