def solution(numbers, hand):
    # numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    # "LRLLLRLLRRL"
    L_button = ['*', 7, 4, 1]
    R_button = ['#', 9, 6, 3]
    C_button = [0, 8, 5, 2]
    
    L_hand_current_index = 0
    R_hand_current_index = 0
    answer = []

    for number in numbers:
        print("왼", L_hand_current_index , " 오: ", R_hand_current_index, "눌러야할 숫자: ", number)
        if number in L_button:
            answer.append('L')
            L_hand_current_index = L_button.index(number)
        elif number in R_button:
            answer.append('R')
            R_hand_current_index = R_button.index(number)
        else:
            # 각 손의 거리는 어떻게 측정할까?? 음.. 일단 인덱스 위치로 확인 가능할듯.
            C_button_index = C_button.index(number) #먼저 중앙 버튼의 인덱스 위치를 구하고, 
            # 인덱스의 거리가 0 , 거리가 1, 거리가 2, 거리가 3 차이나는 것을 찾는다. 절대 값으로 찾을 수 있다.
            L_hand_distance = abs(C_button_index - L_hand_current_index)
            R_hand_distance = abs(C_button_index - R_hand_current_index)

            if L_hand_distance > R_hand_distance: 
                #왼손이 거리가 더 멀다면
                answer.append('R')
                # 왼손의 위치를 바꿔줌.
                L_hand_current_index = C_button_index
            elif L_hand_distance < R_hand_distance:
                #오른손이 거리가 더 멀다면
                answer.append('L')
                # 오른손의 위치를 바꿔줌.
                R_hand_current_index = C_button_index
            else:
                #둘이 같다면
                if hand == 'right':
                    answer.append('R')
                    R_hand_current_index = C_button_index
                else:
                    answer.append('L')
                    L_hand_current_index = C_button_index
    return "".join(answer)

a = solution( [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
