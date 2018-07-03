#Able to merge the node data and to add up, but couldn't convert the added sum
#to convert to LINKEDLIST which is the requested output of the problem
import math
def sum_reversed_lists(llst1, llst2):
	sum1 = summed_up(llst1)
	sum2 = summed_up(llst2)
	num = sum1 + sum2
	return int(num)
	# length = len(str(num))
	# power = length - 1
	# return num_to_llist(num, power)


def summed_up(lst):
	i = 0
	sum = 0
	while lst:
		sum = sum + lst.data * math.pow(10, i)
		lst = lst.next
		i += 1
	return sum
class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

# def num_to_llist(num, power):
# 	n = num // math.pow(10, power)
# 	num = num % math.pow(10, power)
# 	p = power - 1
# 	node = Node(int(n))
# 	for i in range(p):
# 		n = num // math.pow(10, p)
# 		num = num % math.pow(10, p)
# 		node.data = int(n)
# 		node = node.next
# 	return node

head1 = Node(7, Node(1, Node(6, None)))
head2 = Node(5, Node(9, Node(2, None)))

print(sum_reversed_lists(head1, head2))
# ll = num_to_llist(head1, head2)
# while ll:
# 	print(ll.data)
# 	ll = ll.next



