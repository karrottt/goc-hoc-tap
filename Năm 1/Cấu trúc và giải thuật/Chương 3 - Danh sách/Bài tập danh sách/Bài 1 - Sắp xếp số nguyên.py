numbers = input("Nhập dãy số nguyên: ") # nhập dãy số
numbers_list = [int(x) for x in numbers.split()] # tách chuỗi và chuyển thành list số nguyên
sorted_numbers = sorted(numbers_list) # sắp xếp dãy số theo thứ tự tăng dần

print("Dãy số sau khi sắp xếp: ", end="")
for num in sorted_numbers:
    print(num, end=" ")