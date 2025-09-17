import networkx as nx
import matplotlib.pyplot as plt
graph = {
    1: [2, 3, 11],
    2: [1, 4, 6],
    3: [1, 4],
    4: [2, 3, 6],
    5: [9, 10],
    6: [2, 4, 7, 8],
    7: [],
    8: [6, 10],
    9: [5, 13],
    10: [5, 8],
    11: [1, 12, 13],
    12: [11, 13],
    13: [9, 11, 12]
}

G = nx.Graph()
for v, neighbors in graph.items():
    for u in neighbors:
        G.add_edge(v, u)

plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title("Đồ thị từ danh sách kề")
plt.show()

plt.clf()

visited = set()
order = []

def dfs(v):
    visited.add(v)
    order.append(v)
    for u in sorted(graph[v]):   # Duyệt theo thứ tự tăng dần số đỉnh
        if u not in visited:
            dfs(u)

a = int(input("Nhập đỉnh bắt đầu DFS: "))
# Chạy DFS từ đỉnh 1
dfs(a)

print("Thứ tự duyệt DFS:", order)