# Kiểu set – tập hợp không thứ tự
S = {2*x+1 for x in range(10)}
A = {1, 2, 3}
B = {2, 3, 4}
print(A.union(B))
print(A.intersection(B))
print(A - B)

# Vì x chạy từ 0 → 9 nên có đúng 10 giá trị.
# Tập S trong Python tự loại bỏ phần tử trùng lặp.
# Do đó len(S) = 10.

A.add(5)
A.union(B) = {1, 2, 3, 4, 5}
# Chỉ thêm được số 5 so với ban đầu.
