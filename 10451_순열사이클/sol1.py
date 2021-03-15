import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 인덱스를 맞추기 위해 맨 앞에 0을 삽입함.
    arr.insert(0, 0)
    # 해당 인덱스를 이미 검사했는지 확인할 리스트.
    checked = [False] * (N + 1)
    # 해당 순열을 임시적으로 담을 리스트.
    temp = []
    # 순열의 갯수를 담을 변수.
    count = 0
    # 인덱스.
    idx = 1
    # 인덱스는 N 이하.
    while idx <= N:
        # 만약 임시 순열 리스트에 이미 값이 있다면 (== 순열 사이클의 완성을 의미)
        if arr[idx] in temp:
            # 일단 체크했으니 True 로
            checked[idx] = True
            # 순열이 완성됐으므로 카운트 + 1
            count += 1
            # 재사용을 위해 임시 순열 리스트를 비워준다
            temp = []
            # 아래는 체크 안한 인덱스를 찾아가기 위해 1부터 올라가는 코드
            idx = 1
            while checked[idx]:
                idx += 1
                # 맨 끝 번호까지 다 체크한 상태라면 탈출.
                if idx > N:
                    break
        else:
            # 현재 임시 순열 리스트에 현재 idx 에 해당하는 값이 없다면
            # 임시 순열 리스트에 넣는다.
            temp.append(idx)
            # 체크했으니 True 로
            checked[idx] = True
            # 값을 인덱스로 바꿔서 순열 이어서 찾아가기
            idx = arr[idx]
    print(count)
