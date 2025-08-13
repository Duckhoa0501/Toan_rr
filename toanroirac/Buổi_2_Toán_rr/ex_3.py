#Truy hồi tuyến tính thuần nhất với hệ số hằng số
def tinh_fibonacci(n):
    """
    Hàm tính số Fibonacci thứ n bằng phương pháp lặp.
    """
    if n <= 0:
        return 0  # F0 = 0
    elif n == 1:
        return 1  # F1 = 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            next_fib = a + b
            a = b
            b = next_fib
        return b

# Kiểm tra các số Fibonacci
print(f"Fibonacci thứ 2 = {tinh_fibonacci(2)}")  # mong đợi: 1
print(f"Fibonacci thứ 3 = {tinh_fibonacci(3)}")  # mong đợi: 2
print(f"Fibonacci thứ 4 = {tinh_fibonacci(4)}")  # mong đợi: 3
print(f"Fibonacci thứ 6 = {tinh_fibonacci(6)}")  # mong đợi: 8
