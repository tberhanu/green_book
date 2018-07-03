class QueueViaStacks ():
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()
	def enque(self, item):
		self.stack1.push(item)
	def deque(self):
		if self.stack2 == []:
			while self.stack1 != []:
				self.stack2.push(self.stack1.pop())
		return self.stack2.pop()

class Stack():
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		if self.items != []:
			return self.items.pop()
		return None
		
	def peek(self):
		return self.items[len(self.item) - 1]
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)


