#This code looks fine, but IDK why it gives ERROR.....
def sort_stack(stack1):
	if stack1 is None or stack1.size == 0:
		return stack1
	stack2 = Stack()
	stack2.push(stack1.pop())

	while stack1.size != 0:
		temp = stack1.pop()
		while temp > stack2.peek() and stack2.size() != 0:
			stack1.push(stack2.pop())
		stack2.push(temp)
	return stack2

class Stack():
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(4)
s.push(3)
print(s.peek())
print("heree")
ss = sort_stack(s)
while ss.size != 0:
	print(ss.pop())








