

def dfs(v):
    visited = [False for _ in range(V+1)]
    to_visits = [v]  # stack
    path = []

    while to_visits:
        v = to_visits.pop()
        if not visited[v]:
            visited[v] = True
            path.append(v)
            to_visits += G[v]

    return path

