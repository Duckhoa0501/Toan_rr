import networkx as nx

# --- B1: Tạo MultiGraph ban đầu ---
G = nx.MultiGraph()
G.add_edges_from([(1, 2), (1, 2), (2, 3)])

print("Cạnh ban đầu:", list(G.edges(keys=True)))

# Thêm cạnh thứ 3 giữa 1 và 2
G.add_edge(1, 2)
print("Sau khi thêm cạnh thứ 3 giữa 1 và 2:", list(G.edges(keys=True)))
print("Số cạnh giữa 1 và 2:", G.number_of_edges(1, 2))

# --- B2: Thử với Graph (đồ thị thường, không cho cạnh trùng) ---
G2 = nx.Graph()
G2.add_edge(1, 2)
G2.add_edge(1, 2)  # thêm cạnh trùng
print("\nGraph với cạnh trùng:", list(G2.edges()))
# => Không lỗi, nhưng cạnh trùng sẽ bị ghi đè (chỉ có 1 cạnh duy nhất)

# --- B3: Thêm cạnh khuyên tại đỉnh 2 ---
print("\nBậc của đỉnh 2 trước khi thêm khuyên:", G.degree(2))
G.add_edge(2, 2)  # cạnh khuyên
print("Bậc của đỉnh 2 sau khi thêm khuyên:", G.degree(2))
# Lưu ý: cạnh khuyên đóng góp 2 vào bậc của đỉnh


# --- B4: Tạo lại bằng DiGraph ---
DG = nx.DiGraph()
DG.add_edges_from([(1, 2), (1, 2), (2, 3)])  # thử thêm cạnh trùng
print("\nCạnh trong DiGraph:", list(DG.edges()))
print("Loại của DG:", type(DG))
