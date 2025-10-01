import heapq

def prim_mst(edges, start=0):
    # Tạo đồ thị vô hướng
    G = {}
    for u, v, w in edges:
        G.setdefault(u, []).append((v, w))
        G.setdefault(v, []).append((u, w))

    visited = set()
    heap = [(0, start, -1)]  # (trọng số, đỉnh hiện tại, đỉnh cha)
    total_weight = 0
    mst_edges = []

    print(f"\n🔍 Chạy Prim từ đỉnh {start}:")
    while heap:
        weight, u, parent = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        total_weight += weight
        if parent != -1:
            print(f"  -> Chọn cạnh ({parent}, {u}) với trọng số {weight}")
            mst_edges.append((parent, u, weight))
        else:
            print(f"  -> Bắt đầu từ đỉnh {u}")

        for v, w in G[u]:
            if v not in visited:
                heapq.heappush(heap, (w, v, u))

    print(f"✅ Tổng trọng số MST: {total_weight}")
    return mst_edges, total_weight


# ---------------- Yêu cầu 1: Thêm đỉnh mới ----------------
edges1 = [
    (0, 1, 1),
    (0, 3, 2),
    (1, 2, 3),
    (1, 4, 2),
    (2, 4, 1),
    (2, 5, 3),
    (3, 5, 2),
    (4, 6, 2),
    (5, 6, 4)
]
print("\n=== yêu cầu 1: Thêm đỉnh 6 và các cạnh mới ===")
prim_mst(edges1, start=0)


# ---------------- yêu cầu 2: Đổi đỉnh bắt đầu ----------------
print("\n=== yêu cầu 2: Bắt đầu từ đỉnh 3 thay vì 0 ===")
prim_mst(edges1, start=3)


# ---------------- yêu cầu 3: Thay đổi trọng số ----------------
edges2 = [
    (0, 1, 1),
    (0, 3, 6),
    (1, 2, 3),
    (1, 4, 2),
    (2, 4, 1),
    (2, 5, 3),
    (3, 5, 2),
    (4, 6, 2),
    (5, 6, 4)
]
print("\n=== Yêu cầu 3: Thay đổi trọng số (0,3) từ 2 -> 6 ===")
prim_mst(edges2, start=0)
