def sinh_so_nhi_phan(n):
    """
    Sinh tất cả các số nhị phân có độ dài n bằng cách duyệt từ 0 đến 2^n - 1
    và chuyển đổi sang dạng nhị phân.
    """
    if n <= 0:
        print("Độ dài phải là số dương.")
        return

    print(f"Các số nhị phân có độ dài {n}:")
    # Số lượng số nhị phân có độ dài n là 2^n
    so_luong_so = 2**n

    for i in range(so_luong_so):
        # Chuyển số thập phân i sang dạng nhị phân
        # Sử dụng f-string với định dạng {i:0{n}b}
        # ':b' để chuyển sang nhị phân
        # '0{n}' để thêm số 0 vào đầu nếu cần, đảm bảo đủ n chữ số
        dang_nhi_phan = f"{i:0{n}b}"
        print(dang_nhi_phan)

sinh_so_nhi_phan(4)
"""
Giải thích:
Tổng cộng có 2^4 = 16
cách tạo: chương trình chạy i từ 0 -> 15 
- Ví dụ i=5 -> Nhị phân là 0101
- Dùng format f"{i:0{4}b}" để ép thành 4 ký tự
Vậy là tất cả các tổ hợp 0/1 độ dài 4 được sinh ra theo thứ tự giống như đếm số tự nhiên nhưng ở hệ nhị phân
"""

def sinh_so_tam_phan(n):
    if n <= 0:
        print(f"Số yêu cầu phải là số dương")
        return
    
    print(f"Các số tam phân có độ dài {n}: ")
    So_Luong_So = 3**n

    for i in range(So_Luong_So):
        # Chuyển i sang hệ 3
        dang_tam_phan = ""
        x = i
        while x > 0:
            dang_tam_phan = str(x % 3) + dang_tam_phan
            x //= 3

        # Thêm số 0 vào đầu cho đủ độ dài n
        dang_tam_phan = dang_tam_phan.zfill(n)
        print(dang_tam_phan)

sinh_so_tam_phan(2)