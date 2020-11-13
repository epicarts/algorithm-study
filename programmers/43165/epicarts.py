# -*- coding: utf-8 -*-


def dsf(numbers, cur_index, target, current_value):
    global count
    if cur_index == len(numbers):
        # DFS 끝까지 들어 갔을때,
        if target == current_value:
            # 타겟과 같으면 리턴
            count += 1
        return

    new_minus = current_value - numbers[cur_index]
    dsf(numbers, cur_index=cur_index + 1, target=target, current_value=new_minus)

    new_plus = current_value + numbers[cur_index]
    dsf(numbers, cur_index=cur_index + 1, target=target, current_value=new_plus)


def solution(numbers, target):
    dsf(numbers=numbers, cur_index=0, target=target, current_value=0)

    answer = 0
    return answer


count = 0

if __name__ == '__main__':
    solution([1, 1, 1, 1, 1], 3)
    print(count)
