numbers = input("Nhập dãy số nguyên: ") # nhập dãy số
numbers_list = [int(x) for x in numbers.split()] # tách chuỗi và chuyển thành list số nguyên

frequency_dict = {} # khởi tạo từ điển
for num in numbers_list:
    if num in frequency_dict:
        frequency_dict[num] += 1 # tăng giá trị nếu số đã có trong từ điển
    else:
        frequency_dict[num] = 1 # thêm cặp key-value mới nếu số chưa có trong từ điển

print("Số lần xuất hiện của từng số trong dãy số: ")
for key, value in frequency_dict.items():
    print("\n(Số {} xuất hiện {} lần.)".format(key, value), end=" ")