#A tree example with traversal technique Inorder, Preorder, Postorder
    #    1
    #   / \
    #  2    3
    # / \
   # 4   5
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def InorderTraversal(root):
	if root:
		InorderTraversal(root.left)
		print(root.val),
		InorderTraversal(root.right)

def PreorderTraversal(root):
	if root:
		print(root.val),
		PreorderTraversal(root.left)
		PreorderTraversal(root.right)

def PostorderTraversal(root):
	if root:
		PostorderTraversal(root.left)
		PostorderTraversal(root.right)
		print(root.val),
#Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print 'Pr-order Traversal'
PreorderTraversal(root)
print '\nIn-order Traversal'
InorderTraversal(root)
print '\nPost-order Traversal'
PostorderTraversal(root)