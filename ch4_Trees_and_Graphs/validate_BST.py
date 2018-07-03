""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import math
def checkBST(root):
    minimum = float("-inf")
    maximum = float("inf")
    return validate_bst(root, minimum, maximum)
    
def validate_bst(root, minimum, maximum):

    if root == None:
        return True 
    if root.data <= minimum or root.data >= maximum:
        return False 
    return validate_bst(root.left, minimum, root.data) and validate_bst(root.right, root.data, maximum)


