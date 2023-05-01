# Hàm kiểm tra xem ô (x, y) có phải là ô hợp lệ trên bàn cờ hay không
def is_valid(x, y, board):
    if x >= 0 and y >= 0 and x < len(board) and y < len(board) and board[x][y] == -1:
        return True
    return False

# Hàm giải bài toán mã đi tuần bằng thuật toán quay lui
def solveKT(n):
    # Khởi tạo bàn cờ với tất cả các ô chưa được đi qua
    board = [[-1 for i in range(n)]for i in range(n)]

    # Khởi tạo các bước di chuyển của con mã
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Đánh dấu ô (0, 0) là ô bắt đầu của con mã
    board[0][0] = 0

    # Bắt đầu thực hiện thuật toán quay lui từ ô (0, 0)
    if not solveKTUtil(0, 0, 1, board, move_x, move_y):
        print("Không tìm thấy lời giải")
    else:
        print_board(board)

# Hàm thực hiện thuật toán quay lui để tìm đường đi của con mã trên bàn cờ
def solveKTUtil(x, y, movei, board, move_x, move_y):
    if movei == len(board)*len(board):
        return True

    # Thử tất cả các bước di chuyển của con mã
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if is_valid(next_x, next_y, board):
            board[next_x][next_y] = movei
            if solveKTUtil(next_x, next_y, movei+1, board, move_x, move_y):
                return True

            # Nếu không tìm thấy lời giải, trả về trạng thái ban đầu của ô (next_x, next_y)
            board[next_x][next_y] = -1

    return False

# Hàm in bàn cờ
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()

# Sử dụng hàm solveKT() để giải bài toán mã đi
solveKT(8)
