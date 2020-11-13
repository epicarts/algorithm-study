def dfs(depart, tickets, visited):
    global answers

    if not tickets:
        # 추후 정렬을 쉽게하기 위하여, 문자열상태로 유지
        answers.append("".join(visited))
        return

    for i, ticket in enumerate(tickets):  # 현재 낭아 있는 티켓을 확인
        if ticket[0] == depart:  # 출발지가 여기인 곳이 있다면 출발!
            visited.append(ticket[1])  # 방문 국가 추가!

            used_tickets = tickets[:]  # 깊은 복사를 사용 (사용하지 않으면 계속 같은 티켓을 사용함)
            used_tickets.remove(ticket)  # 티켓 사용
            dfs(depart=ticket[1], tickets=used_tickets, visited=visited)
            visited.pop()  # 방문한 국가를 나왔으므로 pop


answers = []


def solution(tickets):
    dfs("ICN", tickets[:], visited=["ICN"])
    answers.sort()

    # 3글자씩 자르기
    answer = [answers[0][i:i + 3] for i in range(0, len(answers[0]), 3)]
    print(answer)
    return answer


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
solution(tickets)
