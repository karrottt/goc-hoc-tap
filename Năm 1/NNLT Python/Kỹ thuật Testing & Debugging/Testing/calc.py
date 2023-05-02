def add(x, y):
    """Hàm cộng"""
    return x + y

def subtract(x, y):
    """Hàm trừ"""
    return x -y

def multiply(x, y):
    """Hàm nhân"""
    return x * y

def devide(x, y):
    """Hàm chia"""
    if y == 0:
        raise ValueError("Không thể chia cho 0!")
    return x / y


