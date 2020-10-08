def solution(n, arr1, arr2):
    answers = []
    for i in range(n):
        bin_answer = bin(arr1[i] | arr2[i])            
        answer = bin_answer[2:].zfill(n).replace('0',' ').replace('1', '#')
        answers.append(answer)
    return answers
