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
