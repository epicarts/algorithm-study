def solution(board, moves):
    stack = []
    count = 0
    transposed = list(zip(*board)) # 변환
    board = [[i for i in b if i != 0] for b in transposed] # 0에 대해서 

    for i, move in enumerate(moves):
        if not board[move-1]:
            continue

        if stack and board[move-1][0] == stack[-1]:
            #기존에 들어간게 있으면,
            stack.pop()
            count += 2
        else:
            #그렇지 않으면, 스택 추가
            stack.append(board[move-1][0])

        #보드에서 제거
        board[move-1].pop(0)
    return count
