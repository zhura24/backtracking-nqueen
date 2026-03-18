n = 4

board = [[0 for x in range(n)] for y in range(n)]

def print_board():
    for row in board:
        print(' '.join('Q' if x == 1 else '.' for x in row))
    print()

def is_safe(row, col):
    # cek kiri
    for i in range(col):
        if board[row][i] == 1:
            return False

    # cek diagonal kiri atas
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # cek diagonal kiri bawah
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(col):
    if col >= n:
        return True

    for i in range(n):
        print(f"Coba taruh di baris {i}, kolom {col}")
        
        if is_safe(i, col):
            board[i][col] = 1
            print_board()

            if solve(col + 1):
                return True

            # BACKTRACK
            print(f"Backtrack dari baris {i}, kolom {col}")
            board[i][col] = 0
            print_board()

    return False

# MAIN
if solve(0):
    print("Solusi ditemukan:")
    print_board()
    exit()   # STOP program setelah solusi ketemu
else:
    print("Tidak ada solusi")