class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right=None

root = TreeNode(10)
root.left =TreeNode(20)
root.right=TreeNode(30)

print("루트",root.data)
print("왼쪽 자식",root.left.data)
print("오른쪽 자식",root.right.data)     

# -------------------

class TreeNode2:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right= None

root = TreeNode(10)

root.left =TreeNode(20)
root.right=TreeNode(30)  

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)

root.right.left = TreeNode(60)
root.right.right = TreeNode(70)
print("루트",root.data)
print("2단계 자식",root.left.data, root.right.data)
print("3단계 자식",root.left.right.data,
      root.left.right.data,root.right.left.data,
      root.right.right.data) 
#          10
#     20        30    
#   40  50   60    70

# 전위순회
# 루트->왼쪽->오른쪽

def preorder(node):
    if node is not None:
        print(node.data, end=" ") 
        preorder(node.left)
        preorder(node.right)
print("전위순회")
preorder(root)

# 중위순회 : 왼쪽->루트->오른쪽
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ") 
        inorder(node.right)

print("\n중위순회")
inorder(root)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

print("\n후위순회")
postorder(root)
