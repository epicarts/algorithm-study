def solution(s, n):
    answer = []
    for i in s:
        #단어를 하나씩 돈다.
        if i == ' ':
            answer.append(' ')
            continue    #공백일 경우 패스
        if 65 <= ord(i) and ord(i) <= 90: #대문자일 경우
            result = ord(i) + n
            if 90 < result:
                result = result - 26
            answer.append(chr(result))
        elif 97 <= ord(i) and ord(i) <= 122: # 소문자일 경우
            result = ord(i) + n
            if 122 < result:
                result = result - 26
            answer.append(chr(result))
    return ''.join(answer)




s = "AB"
n = 1
solution(s, n)