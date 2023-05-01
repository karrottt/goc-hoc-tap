import anytree as cay
from anytree import Node, RenderTree, NodeMixin

#Tạo Node với các giá trị cố định (Tên, Children, hàm append)
class Node:
    def __init__(self, ten):
        self.ten = ten
        self.children = []

    def them_cay(self, node):
        self.children.append(node)

def tao_cay():
    root_value = input("Nhập giá trị gốc: ")
    root = Node(root_value)

    node_queue = [root]
    while len(node_queue) > 0:
        current_node = node_queue.pop(0)
        num_children = int(input(f"Nhập số lượng con của gốc {current_node.ten}: "))
        for i in range(num_children):
            child_value = input(f"Giá trị con của gốc thứ {i+1}: ")
            child_node = Node(child_value)
            current_node.them_cay(child_node)
            node_queue.append(child_node)

    return root
goc = tao_cay()
for pre, _, node in RenderTree(goc):
    print("%s%s" % (pre, node.ten))

def duyet_theo_thu_tu_sau(node):
    if node is not None:
        for children in node.children:
            duyet_theo_thu_tu_sau(children)
        print(node.ten)
print("Duyệt theo thứ tự sau: ")    
duyet_theo_thu_tu_sau(goc)

#Duyệt theo thứ tự trước
def duyet_theo_thu_tu_truoc(node):
    if node is not None:
        print(node.ten)
        for children in node.children:
            duyet_theo_thu_tu_truoc(children)
print("Duyệt theo thứ tự trước: ")      
duyet_theo_thu_tu_truoc(goc)