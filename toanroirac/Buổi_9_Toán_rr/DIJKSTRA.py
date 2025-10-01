import heapq
# Thuật toán Dijkstra
def dijkstra(G, start):
    n = len(G)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (khoảng cách, đỉnh)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in G[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
# Thuật toán Bellman-Ford
def bellman_ford(G, start):
    edges = []
    for u in G:
        for v, w in G[u]:
            edges.append((u, v, w))

    n = len(G)
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


# 1. Đồ thị gốc
print("=== ĐỒ THỊ GỐC ===")
G1 = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: []
}
print("Dijkstra:", dijkstra(G1, 0))
print("Bellman-Ford:", bellman_ford(G1, 0))
# 2. Thay đổi trọng số cạnh (0,2) = 1
print("\n=== THAY ĐỔI CẠNH (0,2) = 1 ===")
G2 = {
    0: [(1, 1), (2, 1)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: []
}
print("Dijkstra:", dijkstra(G2, 0))
print("Bellman-Ford:", bellman_ford(G2, 0))
# 3. Đồ thị khác (5 đỉnh)
print("\n=== ĐỒ THỊ MỚI 5 ĐỈNH ===")
G3 = {
    0: [(1, 2), (2, 6)],
    1: [(2, 3), (3, 1)],
    2: [(3, 1), (4, 5)],
    3: [(4, 2)],
    4: []
}
print("Dijkstra:", dijkstra(G3, 0))
print("Bellman-Ford:", bellman_ford(G3, 0))
