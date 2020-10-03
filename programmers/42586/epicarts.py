import collections
import math

def solution(progresses, speeds):
    deq = collections.deque()
    answer = []

    for i, progress in enumerate(progresses):
        deq.append(math.ceil(((100 - progress) / speeds[i])))

    stack = []
    for q in deq:
        if not stack:
            stack.append(q)
        elif stack and stack[0] >= q: # 마지막 스택이랑 비교
            stack.append(q)
        else:
            answer.append(len(stack))
            stack = [q]
    answer.append(len(stack))

    return answer



if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))
