# Thuật toán Kruskal
def kruskal(n, edges):
    edges.sort()  # sắp xếp theo trọng số
    parent = list(range(n))

    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    mst = []
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
    return mst


# --- Trường hợp 1: Đồ thị ban đầu (4 đỉnh) ---
edges1 = [(1,0,1), (3,0,2), (4,1,2), (2,1,3), (5,2,3)]
mst1 = kruskal(4, edges1)
print("MST ban đầu:", mst1, "Tổng trọng số =", sum(w for _,_,w in mst1))

# Thêm cạnh (1,3,6)
edges1_new = edges1 + [(6,1,3)]
mst1_new = kruskal(4, edges1_new)
print("MST sau khi thêm (1,3,6):", mst1_new, "Tổng trọng số =", sum(w for _,_,w in mst1_new))


# --- Trường hợp 2: Đồ thị 6 đỉnh ---
edges2 = [
    (4,0,1), (3,0,2), (1,1,2), (2,1,3),
    (4,2,3), (2,3,4), (6,4,5), (7,2,5)
]
mst2 = kruskal(6, edges2)
print("MST đồ thị 6 đỉnh:", mst2, "Tổng trọng số =", sum(w for _,_,w in mst2))


# --- Trường hợp 3: Thay đổi trọng số (0,1) từ 1 -> 3 ---
edges3 = [(3,0,1), (3,0,2), (4,1,2), (2,1,3), (5,2,3)]
mst3 = kruskal(4, edges3)
print("MST sau khi thay đổi trọng số của cạnh (0,1) từ 1 thành 3 là:", mst3, "Tổng trọng số =", sum(w for _,_,w in mst3))

