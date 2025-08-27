import math

def ap_dung_dirichlet_tong_quat(n_chim, m_chuong):
    """
    Tính toán số chim tối thiểu trong một chuồng theo Nguyên lý Dirichlet dạng tổng quát.
    n_chim: số lượng chim bồ câu (ví dụ: số người)
    m_chuong: số lượng chuồng (ví dụ: số tháng trong năm)
    """
    if m_chuong <= 0:
        return "Số chuồng phải lớn hơn 0."

    # Sử dụng math.ceil để làm tròn lên 
    so_chim_toi_thieu = math.ceil(n_chim / m_chuong)

    print(f"Có {n_chim} 'chim bồ câu' và {m_chuong} 'chuồng'.")
    print(f"Theo Nguyên lý Dirichlet, ít nhất có một 'chuồng' chứa: {so_chim_toi_thieu} 'chim bồ câu' trở lên.")
    return so_chim_toi_thieu

def ap_dung_dirichlet_nguoc(m_chuong, k):
    """
    Bài toán ngược: tìm số lượng tối thiểu cần rút để chắc chắn có k con 'chim' trong một chuồng.
    m_chuong: số chuồng (ví dụ: số màu bóng)
    k: số lượng cần cùng loại (ví dụ: 20 quả cùng màu)
    """
    if m_chuong <= 0 or k <= 0:
        return "Số chuồng và k phải lớn hơn 0."
    
    so_chim_can_rut = (k - 1) * m_chuong + 1
    print(f"Với {m_chuong} 'chuồng' và cần ít nhất {k} 'chim' trong 1 chuồng:")
    print(f"=> Phải rút ra ít nhất {so_chim_can_rut} 'chim'.")
    return so_chim_can_rut

print(f"Bài 1: 400 học sinh, 365 ngày")
ap_dung_dirichlet_tong_quat(400, 365)

print(f"Bài 2: 200 kẹo 3 cái túi")
ap_dung_dirichlet_tong_quat(200, 3)

print(f"Bài 3: 100 quả bóng, 5 màu cần >=20 quả cùng màu")
ap_dung_dirichlet_nguoc(5,20)