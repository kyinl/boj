import sys
sys.stdin = open('input.txt')

# 세로 M, 가로 N 직사각형 안에 K개의 직사각형
M, N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(K)]
# 색칠할 빈 NxM 행렬
checked = [[False] * N for _ in range(M)]
# 각종 변수들
colored = []
temp = []
area = 0
areas = []
# 델타
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# True 로 색칠하기
# r for rectangle
for r in matrix:
    for x in range(r[0], r[2]):
        for y in range(r[1], r[3]):
            temp.append((x, y))
    for tup in temp:
        if tup not in colored:
            colored.append(tup)
    temp = []

for x, y in colored:
    checked[y][x] = True

# bfs 로 검사하기
# False 인 곳을 발견하면 True 로 채운다.
for y in range(M):
    for x in range(N):
        # False 인 곳 첫 발견
        if not checked[y][x]:
            # 일단 넓이는 1
            area = 1
            # 일단 True 로 채운다
            checked[y][x] = True
            # 큐에 좌표를 넣는다
            queue = [[y, x]]
            # 델타를 이용해 이동하면서 죄다 True 로 채운다
            while queue:
                y, x = queue[0][0], queue[0][1]
                del queue[0]
                for i in range(4):
                    y_ = y + dy[i]
                    x_ = x + dx[i]
                    if 0 <= y_ < M and 0 <= x_ < N and checked[y_][x_] is False:
                        checked[y_][x_] = True
                        area += 1
                        queue.append([y_, x_])
            # 다 채웠으면 넓이들 리스트에 넓이를 넣는다
            areas.append(area)
# 넓이들의 갯수 출력
print(len(areas))
# 넓이들 정렬
areas.sort()
# 넓이들 출력
print(*areas)
