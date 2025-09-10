import networkx as nx
import matplotlib.pyplot as plt

# --- B1: Tạo đồ thị có hướng ban đầu ---
G = nx.DiGraph()
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")])

# --- B2: Thêm cạnh D→A ---
G.add_edge("D", "A")

# Kiểm tra đồ thị có chu trình không
has_cycle = not nx.is_directed_acyclic_graph(G)
print("Đồ thị có chu trình không?", has_cycle)

# --- B3: In successors và predecessors ---
print("Các đỉnh kề sau (successors) của A:", list(G.successors("A")))
print("Các đỉnh kề trước (predecessors) của D:", list(G.predecessors("D")))

# --- B4: Đổi hướng cạnh (A→C) thành (C→A) ---
if G.has_edge("A", "C"):
    G.remove_edge("A", "C")
G.add_edge("C", "A")

# --- Vẽ đồ thị sau các thay đổi ---
pos = nx.spring_layout(G, seed=42)  # layout đẹp, cố định seed cho dễ quan sát
nx.draw(G, pos, with_labels=True, node_color='lightgreen',
        node_size=1000, arrowsize=20, width=2)

plt.title("Đồ thị có hướng sau các thay đổi")
plt.show()

# --- B5: Kiểm tra lại tính DAG ---
print("Đồ thị có phải DAG không?", nx.is_directed_acyclic_graph(G))