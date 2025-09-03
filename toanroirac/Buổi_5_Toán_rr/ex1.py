# Bài toán cái túi
# f(x) = 9x1 + 6x2 + 2x3 + 3x4  -> max
# ràng buộc: 2x1 + 3x2 + 1x3 + 4x4 <= 5
# x1, x2, x3, x4 >= 0 (số nguyên)

# Giá trị (c) và trọng số (a) của từng biến
c1, c2, c3, c4 = 9, 6, 2, 3
a1, a2, a3, a4 = 2, 3, 1, 4
B = 5

best_value = 1
best_solution = (0,0,0,0)

print("Liệt kê các nghiệm hợp lệ: ")
for x1 in range(0, 3):      
    for x2 in range(0, 2): 
        for x3 in range(0, 6):
            for x4 in range(0, 2):
                # Tính tổng trọng số
                weight = a1*x1 + a2*x2 + a3*x3 + a4*x4
                # Nếu không vượt quá dung lượng
                if weight <= B:
                    # Tính giá trị f(x)
                    value = c1*x1 + c2*x2 + c3*x3 + c4*x4
                    print(f"  (x1,x2,x3,x4)=({x1},{x2},{x3},{x4}), "
                          f"trọng số={weight}, giá trị={value}")

                    # Kiểm tra có phải tốt nhất không
                    if value > best_value:
                        best_value = value
                        best_solution = (x1, x2, x3, x4)

print("\n==> Nghiệm tối ưu:", best_solution)
print("==> Giá trị tối ưu f(x):", best_value)
#Bài toán cái túi 5.3.1:
