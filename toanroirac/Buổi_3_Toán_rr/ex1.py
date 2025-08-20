import random
def mo_phong_rut_tat(so_luong_rut):
    """
    Mô phỏng việc rút tất từ ngăn kéo và kiểm tra có đôi tất cùng màu hay không.
    Ngăn kéo có: 5 đôi tất đen (10 chiếc), 5 đôi tất trắng (10 chiếc).
    """
    tat_trong_ngan_keo = ['đen'] * 10 + ['trắng'] * 10

    # Trộn ngẫu nhiên các chiếc tất
    random.shuffle(tat_trong_ngan_keo)

    # Rút ra số lượng tất yêu cầu
    tat_da_rut = tat_trong_ngan_keo[:so_luong_rut]

    # Đếm số lượng tất đen và trắng đã rút được
    dem_den = tat_da_rut.count('đen')
    dem_trang = tat_da_rut.count('trắng')

    print(f"Bạn đã rút ra: {tat_da_rut}")
    print(f"Số tất đen: {dem_den}, Số tất trắng: {dem_trang}")

    # Kiểm tra xem có đôi tất cùng màu hay không (ít nhất 2 chiếc cùng màu)
    if dem_den >= 2 or dem_trang >= 2:
        print("=> CHẮC CHẮN CÓ MỘT ĐÔI TẤT CÙNG MÀU (theo Nguyên lý Dirichlet)!")
        return True
    else:
        print("=> CHƯA CHẮC CHẮN có đôi tất cùng màu.")
        return False

print("--- Mô phỏng rút 2 chiếc tất ---")
mo_phong_rut_tat(2) # Thử chạy vài lần để thấy kết quả có thể chưa chắc chắn

print("\n--- Mô phỏng rút 3 chiếc tất ---")
mo_phong_rut_tat(3) # Thử chạy vài lần, bạn sẽ thấy kết quả luôn là "CHẮC CHẮN CÓ MỘT ĐÔI"
mo_phong_rut_tat(3)
mo_phong_rut_tat(3)

# Giải thích:
# Trường hợp 2 màu đen trắng 
# Ngăn kéo ban đầu có 10 tất đen + 10 tất trắng
# Khi rút 2 chiêc tất: 
# - Nếu cả hai cùng màu đen đen, trắng trắng -> có đôi tất cùng màu
# - Nếu rút ra 1 đen 1 trắng -> không có đôi tất cùng màu
# --> vì vậy mô phỏng rút 2 tất có thể thấy đôi khi cùng màu đôi khi khác màu  
# Điều này đúng với nguyên lý dirichlet (Nguyễn lý lồng chim)
# - với 2 màu, cần rút 3 chiếc thì chắc chắn có 1 đôi cùng màu
# - Với 2 chiếc thì chưa đảm bảo

# Yêu cầu 2:
import random
def mo_phong_rut_tat(so_luong_rut):
    """
    Mô phỏng rút tất từ ngăn kéo và kiểm tra xem có đôi tất cùng màu hay không:
    - 10 chiếc tất đen
    - 10 chiếc tất trắng
    - 6 chiếc tất xám
    """
    tat_trong_ngan_keo = ['Đen'] * 10 + ['Trắng']*10 + ['Xám'] * 6

    random.shuffle(tat_trong_ngan_keo)

    tat_da_rut = tat_trong_ngan_keo[:so_luong_rut]

    dem_den = tat_da_rut.count('Đen')
    dem_trang = tat_da_rut.count('Trắng')
    dem_xam = tat_da_rut.count('Xám')

    print(f"Bạn đã rút ra: {tat_da_rut}")
    print(f"Số tất Đen: {dem_den}, Trắng: {dem_trang}, Xám: {dem_xam}")

    if dem_den >= 2 or dem_trang >= 2 or dem_xam >= 2:
        print("=> CHẮC CHẮN CÓ MỘT ĐÔI TẤT CÙNG MÀU (Dirichlet)!")
        return True
    else:
        print("=> CHƯA CHẮC CHẮN có đôi tất cùng màu.")
        return False
    
print("\n--- Mô phỏng rút 3 chiếc tất (có thể chưa chắc chắn) ---")
for _ in range(3):
    mo_phong_rut_tat(3)

print("\n--- Mô phỏng rút 4 chiếc tất (luôn chắc chắn có đôi) ---")
for _ in range(3):
    mo_phong_rut_tat(4)