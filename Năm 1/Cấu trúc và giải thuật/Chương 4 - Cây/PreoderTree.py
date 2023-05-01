
class Node:
    def __init__(self, data):
        self.left_child = None      # Khởi tạo giá trị self.left_child là None
        self.right_child = None     # Khởi tạo giá trị self.right_child là None
        self.parent_node = data     # Khởi tạo giá trị self.parent_node là data

    # Thực hiện in ra các giá trị của các nút theo thứ tự trước duyệt cây
    def print_tree(self):
        # Nếu "NÚT CON BÊN TRÁI" tồn tại, in ra giá trị của "NÚT CON BÊN TRÁI"
        if self.left_child:
            self.left_child.print_tree()

        # In "NÚT CHA" ở trung tâm
        print(self.parent_node)

        # Nếu "NÚT CON BÊN PHẢI" tồn tại, in ra giá trị của "NÚT CON BÊN PHẢI"
        if self.right_child:
            self.right_child.print_tree()

    # Chèn 1 giá trị mới vào cây
    def insert_number(self, input_number):
        # Kiểm tra "NÚT CHA" hiện tại đã tồn tại hay chưa
        if self.parent_node:    # Nếu đã tồn tại, so sánh giá trị mới với "NÚT CHA" hiện tại
            # Nếu số đầu vào nhỏ hơn "NÚT CHA" thì nó nằm ở bên trái
            if input_number < self.parent_node:
                # Kiểm tra "NÚT CON BÊN TRÁI" có tồn tại hay không
                if self.left_child is None:     # Nếu không có, tạo một nút mới với giá trị đầu vào và gán nó cho "self.left_child"
                    self.left_child = Node(input_number)
                else:                           # Nếu có, đệ quy vào "nút con bên trái" và gọi hàm "insert_number" với giá trị đầu vào để tiếp tục kiểm tra và chèn giá trị vào cây
                    self.left_child.insert_number(input_number)

            # Nếu số đầu vào lớn hơn nút cha thì nó nằm ở bên phải
            elif input_number > self.parent_node:
                # Kiểm tra "NÚT CON BÊN PHẢI" có tồn tại hay không
                if self.right_child is None:    # Nếu không có, tạo một nút mới với giá trị đầu vào và gán nó cho "self.right_child"
                    self.right_child = Node(input_number)
                else:                           # Nếu có, đệ quy vào "nút con bên phải" và gọi hàm "insert_number" với giá trị đầu vào để tiếp tục kiểm tra và chèn giá trị vào cây
                    self.right_child.insert_number(input_number)
        else:   # Nếu chưa tồn tại, sẽ tạo 1 nút mới với giá trị mới và gán cho nó thuộc tính "self.parent_node"
            self.parent_node = input_number

root = Node(7)
root.insert_number(1)
root.insert_number(5)
root.insert_number(9)
root.insert_number(70)
root.insert_number(2)
root.insert_number(3)
root.insert_number(6)
root.insert_number(4)
root.insert_number(69)

#
root.print_tree()