class Queue():
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.insert(0, item)
	def dequeue(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []
	def peek(self):
		return self.items[len(self.items) - 1]
	def size(self):
		return len(self.items)
