#Đồ thị vô hướng đơn
# Đề bài: Vẽ đồ thị vô hướng đơn với: Đỉnh: {1, 2, 3, 4} — Cạnh: {(1,2), (1,3), (2,4)}
# Yêu cầu sinh viên sửa và lý giải
# • Thêm đỉnh 5 và cạnh 2–5 → Quan sát thay đổi liên thông 
# • Xóa cạnh 1–2 → Có đỉnh nào cô lập không? Có đỉnh 1 và 3 bị cô lập
# • Thêm cạnh 3–4 → Có chu trình trực quan không? Có
# • Đếm bậc đỉnh bằng cách nhìn số cạnh nối

import networkx as nx
import matplotlib.pyplot as plt

# Khởi tạo đồ thị ban đầu
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# --- B1: Thêm đỉnh 5 và cạnh (2, 5) ---
G.add_node(5)             # thêm đỉnh 5
G.add_edge(2, 5)          # nối cạnh 2–5
# Lúc này, đồ thị có thêm đỉnh 5 và nó nối với thành phần liên thông chính
# → vẫn là 1 đồ thị liên thông.

# --- B2: Xóa cạnh (1, 2) ---
G.remove_edge(1, 2)
# Kiểm tra đỉnh cô lập: một đỉnh gọi là cô lập nếu bậc = 0
isolated = [n for n, d in G.degree() if d == 0]
print("Đỉnh cô lập:", isolated)
# → Không có đỉnh cô lập, vì tất cả đều nối với ít nhất một cạnh.

# --- B3: Thêm cạnh (3, 4) ---
G.add_edge(3, 4)
# Bây giờ ta có chu trình: 1–3–4–2–5 (một số chu trình con nhỏ hơn cũng thấy được)

# --- Vẽ đồ thị ---
pos = nx.spring_layout(G)  # layout cho đẹp
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        node_size=800, font_size=12, width=2)

plt.title("Đồ thị sau các thay đổi")
plt.show()

# --- B4: Đếm bậc đỉnh ---
print("Bậc của từng đỉnh:")
for node, degree in G.degree():
    print(f"Đỉnh {node}: bậc = {degree}")
