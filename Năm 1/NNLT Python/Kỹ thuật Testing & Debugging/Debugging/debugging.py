password = input("Vui lòng nhập mật khẩu: ")
x = bool
y = bool  # True/False



while True:
    for i in password:
        if i.isdigit():
            x = True
            break
        else:
            x = False

    for i in password:
        if i.isalpha():
            y = True
            break
        else:
            y = False

    if len(password) < 6 or x == False or y == False:
        password = input("Vui lòng nhập lại mật khẩu "
                        "(có ít nhất 6 ký tự, chứa ít nhất 1 chữ cái và 1 số): ")
    else:
        print("Mật khẩu hợp lệ.")
        break

login = input("Vui lòng nhập mật khẩu: ")
count = 0
while login != password:
    count += 1
    login = input(f"Vui lòng nhập lại mật khẩu. Nhập sai {count}/5 lần : ")
    if count == 5:
        print("Bạn nhập sai mật khẩu quá 5 lần, khóa đăng nhập.")
        break
else:
    print("Đăng nhập thành công")




