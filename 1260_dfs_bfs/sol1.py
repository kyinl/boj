import sys
sys.stdin = open('dfs_bfs_input.txt')


def dfs(M, N, V, graph):

    visited = [False for _ in range(N+1)]
    # 가야할 곳
    to_visits = [V]
    # 탐색중에 걸어온 길
    path = []
    while to_visits:
        current = to_visits.pop()
        if not visited[current]:
            visited[current] = True
            path.append(current)
            # 갔든지 안갔든지 다 넣는다.
            # 아래 코드 생략가능
            # for v in graph[current]:
            #     if not visited[v]:
            #         to_visits.append(v)

            # 내림차순 정렬
            to_visits += sorted(graph[current])[::-1]
    # print(path)
    return path


def bfs(M, N, V, graph):
    visited = [False for _ in range(N + 1)]
    # 가야할 곳
    to_visits = [V]
    # 탐색중에 걸어온 길
    path = []
    while to_visits:
        # dfs 코드에서 pop 에 0 넣고 정렬을 오름차순으로 하면 bfs 가 된다.
        current = to_visits.pop(0)
        if not visited[current]:
            visited[current] = True
            path.append(current)
            # 갔든지 안갔든지 다 넣는다.
            # 아래 코드 생략가능
            # for v in graph[current]:
            #     if not visited[v]:
            #         to_visits.append(v)

            # 오름차순 정렬
            to_visits += sorted(graph[current])
    # print(path)
    return path


T = int(input())
for tc in range(1, T+1):
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    print(dfs(M, N, V, graph))
    print(bfs(M, N, V, graph))

