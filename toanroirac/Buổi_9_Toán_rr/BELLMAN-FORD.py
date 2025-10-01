def bellman_ford(edges, n, start=0):
    dist = [float('inf')] * n
    dist[start] = 0

    # Bước 1: Lặp n-1 lần để cập nhật
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Bước 2: Kiểm tra chu trình âm
    negative_cycle = False
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            negative_cycle = True
            break

    return dist, negative_cycle


# ---------------- Yêu cầu 1: Thêm cạnh âm ----------------
edges1 = [(0, 1, 1), (0, 2, 4), (1, 2, -3), (2, 3, 2), (3, 4, -2)]
n1 = 5
dist1, neg1 = bellman_ford(edges1, n1)

print("=== Yêu cầu 1: Thêm cạnh âm (3,4,-2) ===")
print("Khoảng cách ngắn nhất từ 0:", dist1)
print("Chu trình âm:", "Có" if neg1 else "Không")
print("-" * 50)


# ---------------- Yêu cầu 2: Chu trình âm ----------------
edges2 = [(0, 1, 1), (0, 2, 4), (1, 2, -3), (2, 3, -6), (3, 2, 4)]
n2 = 4
dist2, neg2 = bellman_ford(edges2, n2)

print("=== Yêu cầu 2: Thêm chu trình âm (2↔3) ===")
print("Khoảng cách ngắn nhất từ 0:", dist2)
print("Chu trình âm:", "Có" if neg2 else "Không")
print("-" * 50)


# ---------------- Yêu cầu 3: Không có cạnh âm ----------------
edges3 = [(0, 1, 4), (0, 2, 5), (1, 2, 1), (2, 3, 2)]
n3 = 4
dist3, neg3 = bellman_ford(edges3, n3)

print("=== Yêu cầu 3: Đồ thị không có cạnh âm ===")
print("Khoảng cách ngắn nhất từ 0:", dist3)
print("Chu trình âm:", "Có" if neg3 else "Không")
print("-" * 50)