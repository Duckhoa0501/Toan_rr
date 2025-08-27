import itertools

def liet_ke_hoan_vi(danh_sach_phan_tu):
    """
    Liệt kê tất cả các hoán vị của một danh sách các phần tử bằng thuật toán quay lui.
    """
    ket_qua = [] # Danh sách để lưu trữ tất cả các hoán vị tìm được
    n = len(danh_sach_phan_tu)

    # Hàm trợ giúp đệ quy (hàm con)
    # path: hoán vị hiện tại đang được xây dựng
    # remaining: các phần tử còn lại chưa được sử dụng
    def backtrack(current_permutation, remaining_elements):
        # Điều kiện dừng: nếu không còn phần tử nào, hoán vị đã hoàn thành
        if not remaining_elements:
            ket_qua.append("".join(map(str, current_permutation))) # Thêm hoán vị vào kết quả
            return

        # Duyệt qua từng phần tử còn lại
        for i in range(len(remaining_elements)):
            # Chọn một phần tử
            chon_phan_tu = remaining_elements[i]

            # Đánh dấu phần tử đã chọn (thêm vào hoán vị hiện tại)
            current_permutation.append(chon_phan_tu)

            # Xây dựng danh sách các phần tử còn lại (bỏ phần tử vừa chọn)
            new_remaining = remaining_elements[:i] + remaining_elements[i+1:]

            # Gọi đệ quy cho phần còn lại
            backtrack(current_permutation, new_remaining)

            # Quay lui: bỏ phần tử đã chọn để thử lựa chọn khác
            current_permutation.pop()

    # Bắt đầu quá trình quay lui
    backtrack([], list(danh_sach_phan_tu))
    return ket_qua

# Liệt kê hoán vị của danh sách số [1,2,3,4]
print(liet_ke_hoan_vi([1,2,3,4]))

