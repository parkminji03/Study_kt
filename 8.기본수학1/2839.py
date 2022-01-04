N = int(input())

DP = [0]*(N+1)

if N <= 5:
    for n in range(1, N+1):
        if n % 3 == 0 or n % 5 == 0:
            DP[n] = 1
        else:
            DP[n] = -1

else:
    for n in range(1, 6):
        if n % 3 == 0 or n % 5 == 0:
            DP[n] = 1
        else:
            DP[n] = -1

    for n in range(6, N+1):
        case1 = DP[n-5]
        case2 = DP[n-3]
        if case1 == -1 and case2 == -1:
            DP[n] = -1
        elif case1 == -1:
            DP[n] = case2 + 1
        elif case2 == -1:
            DP[n] = case1 + 1
        else:
            DP[n] = min(case1, case2) + 1

print(DP[N])