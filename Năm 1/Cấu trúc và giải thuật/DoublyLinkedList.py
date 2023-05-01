# Tạo class
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):

        self.head = None

    # Chèn nút vào đầu danh sách
    def insert_at_Head(self, data):
        # 1 & 2: Tạo new_node và thêm dữ liệu
        new_node = Node(data)

        # 3: Con trỏ Next trỏ tới nút đầu và con trỏ Prev trỏ tới Null
        new_node.next = self.head

        # 4.1: Gán con trỏ Prev của nút đầu hiện tại trỏ tới new_node
        if self.head is not None:
            self.head.prev = new_node
        # 4.2: Update lại nút đầu chính là new_node
        self.head = new_node

    # Chèn nút vào cuối danh sách
    def insert_at_Tail(self, data):
        # 1 & 2: Tạo new_node và thêm dữ liệu
        new_node = Node(data)
        last = self.head

        # 3: Node mới nằm ở cuối cùng -> con trỏ Next trỏ tới Null
        new_node.next = None

        # 4: Nếu danh sách trống thì tạo 1 new_node tương tự như nút đầu
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # 5: Lặp lại cho đến khi đi qua nút cuối cùng
        while (last.next is not None):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node
        # 7. Make last node as previous of new node */
        new_node.prev = last

    # Chèn nút vào vị trí bất kỳ - chèn sau nút đã cho
    def insert_at_Position(self, data, position):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        elif position == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current_node = self.head
            i = 1
            while i < position - 1 and current_node.next is not None:
                current_node = current_node.next
                i += 1
            if current_node.next is None:
                current_node.next = new_node
                new_node.prev = current_node
            else:
                new_node.next = current_node.next
                new_node.prev = current_node
                current_node.next.prev = new_node
                current_node.next = new_node

            # Xoá nút đầu danh sách
    def delete_at_Head(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head_prev = None

    # Xóa nút cuối danh sách
    def delete_at_Tail(self):
        # Check if the List is empty
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    # Hiển thị
    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next



#Tạo 1 danh sách liên kết đôi
NewDoublyLinkedList = DoublyLinkedList()

# Thêm nút vào đầu danh sách
print("\nSau khi thêm các nút vào đầu danh sách:")
NewDoublyLinkedList.insert_at_Head(4)
NewDoublyLinkedList.insert_at_Head(3)
NewDoublyLinkedList.insert_at_Head(2)
NewDoublyLinkedList.insert_at_Head(1)
NewDoublyLinkedList.Display()

print()

#Thêm nút vào cuối danh sách
print("\nSau khi đã thêm các nút vào cuối danh sách")
NewDoublyLinkedList.insert_at_Tail(97)
NewDoublyLinkedList.insert_at_Tail(98)
NewDoublyLinkedList.insert_at_Tail(99)
NewDoublyLinkedList.insert_at_Tail(100)
NewDoublyLinkedList.Display()

print()

# Chèn nút ở vị trí chỉ định
print("\nSau khi đã thêm nút (999) vào vị trí thứ 2")
NewDoublyLinkedList.insert_at_Position(999, 2)
NewDoublyLinkedList.Display()
print("\nSau khi đã thêm nút (111) vào vị trí thứ 3")
NewDoublyLinkedList.insert_at_Position(111, 3)
NewDoublyLinkedList.Display()

print()

# Xóa nút ở vị trí đầu của danh sách
print("\nSau khi đã xóa nút ở đầu danh sách:")
NewDoublyLinkedList.delete_at_Head()
NewDoublyLinkedList.Display()

print()

# Xóa nút ở vị trí cuối cùng của danh sách
print("\nSau khi xóa nút ở cuối danh sách:")
NewDoublyLinkedList.delete_at_Tail()
NewDoublyLinkedList.Display()

print()

# In ra nút ở vị trí thứ 3
temp = NewDoublyLinkedList.head
for i in range(1, 3):
    temp = temp.next
print("\nNút thứ 3 trong danh sách là:", temp.data)
