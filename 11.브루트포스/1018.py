row, col = map(int,input().split())

# 정상적인 체스판(8*8) 만들기 (W로 시작, B로 시작하는 체스판 2개)
start_W = [j for i in range(4) for j in ('W','B')]             # start_W : ['W','B','W','B','W','B','W','B']
start_B = [j for i in range(4) for j in ('B','W')]             # start_B : ['B','W','B','W','B','W','B','W']
check_board_B =[]                                              # 'B'로 시작하는 체스판을 만들 빈 리스트 선언
check_board_W =[]                                              # 'W'로 시작하는 체스판을 만들 빈 리스트 선언

for i in range(8):                                             # 정상적인 체스판 채우기
    if i % 2:                                                  # 한 라인은 W 또는 B로 시작하는 리스트
        check_board_B.append(start_W)
        check_board_W.append(start_B)
    else:                                                      # 다음 라인은 B 또는 W로 시작하는 리스트
        check_board_B.append(start_B)
        check_board_W.append(start_W)

# 자를 체스판 입력받기
input_board = []                                               # 입력받을 체스판을 받을 빈 리스트 선언
for i in range(row):
    input_board.append(list(input()))                          # 열 개수만큼 append해주기

# 입력받은 체스판과 정상 체스판을 비교
min_W = 9999                                                   # W로 시작하는 체스판의 칠 개수의 최소값을 구하기 위한 변수 선언
min_B = 9999                                                   # B로 시작하는 체스판의 칠 개수의 최소값을 구하기 위한 변수 선언

for i in range(row-7):                                         # 입력받은 판에서 (8*8)사이즈를 여러번 검사하기 위한 반복문 (열)
    for j in range(col-7):                                     # 입력받은 판에서 (8*8)사이즈를 여러번 검사하기 위한 반복문 (행)
        # (8*8)사이즈만 비교해서 칠해야하는 개수 파악 
        cnt_W = 0                                                # 8*8 사이즈에서 색칠할 개수 세는 변수 (W로 시작하는 경우)
        cnt_B = 0                                                # 8*8 사이즈에서 색칠할 개수 세는 변수 (B로 시작하는 경우)
        for a in range(8):                                       # 8*8 사이즈만 비교
            for b in range(8):
                if input_board[i+a][j+b] != check_board_W[a][b]:
                    cnt_W += 1
                if input_board[i+a][j+b] != check_board_B[a][b]:
                    cnt_B += 1
        if cnt_W <= min_W:                                        # 최소값을 구하기 위한 로직 (W로 시작하는 경우)
            min_W = cnt_W
        if cnt_B <= min_B:                                        # 최소값을 구하기 위한 로직 (B로 시작하는 경우)
            min_B = cnt_B

if min_B >= min_W:                                                # 제일 작은 최소값만 출력해라
    print(min_W)
else:
    print(min_B)
    