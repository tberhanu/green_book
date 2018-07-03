# Stack with push, pop, and min at constant time, O(1)
class MinStack():
	def __init__(self):
		self.items = []
		self.mins = []

	def push(self, item):
		self.items.append(item)
		if self.mins == []:
			self.mins.append(item)
		else:
			if item <= self.mins[len(self.mins) - 1]:
				self.mins.append(item)

	def pop(self):
		top = self.items.pop()
		if top == self.mins[len(self.mins) - 1]:
			self.mins.pop()
		return top

	def peek(self):
		return self.items[len(self.items) - 1]

	def min(self):
		if len(self.mins) == 0:
			return None
		return self.mins[len(self.mins) - 1]

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

import unittest

class Test(unittest.TestCase):
  def test_min_stack(self):
    min_stack = MinStack()
    self.assertEqual(min_stack.min(), None)
    min_stack.push(7)
    self.assertEqual(min_stack.min(), 7)
    min_stack.push(6)
    min_stack.push(5)
    self.assertEqual(min_stack.min(), 5)
    min_stack.push(10)
    self.assertEqual(min_stack.min(), 5)
    self.assertEqual(min_stack.pop(), 10)
    self.assertEqual(min_stack.pop(), 5)
    self.assertEqual(min_stack.min(), 6)
    self.assertEqual(min_stack.pop(), 6)
    self.assertEqual(min_stack.pop(), 7)
    self.assertEqual(min_stack.min(), None)

if __name__ == "__main__":
  unittest.main()

