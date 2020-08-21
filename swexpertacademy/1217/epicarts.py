
def fun(n, c):
    if c == 0:
        return 1
    else:
        return n * fun(n,  c-1)

T =  10
for test_case in range(1, T + 1):
    int(input())
    b, c = map(int, input().split())
    print('#{} {}'.format(test_case, fun(b, c)))