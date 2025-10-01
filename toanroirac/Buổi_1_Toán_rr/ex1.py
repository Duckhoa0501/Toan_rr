# Luận lý python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(a ^ b)    # True
# Ví dụ:
a = True
b = False
print("a and b =", a and b)
print("a or b =", a or b)
print("a ^ b =", a ^ b)
print("not a =", not a)

# Biểu thức điều kiện if
def kiemtra_nuocsoi(nhiet_do):
    if nhiet_do < 100:
        return "Nước chưa sôi"
    elif nhiet_do < 50:
        return "Nước Lạnh"
    else:
        return "Nước đã sôi"
print(kiemtra_nuocsoi(99))
print(kiemtra_nuocsoi(-10))
print(kiemtra_nuocsoi(100))