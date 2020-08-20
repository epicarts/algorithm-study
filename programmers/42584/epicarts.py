def solution(prices):
    answer = [0] * len(prices)

    for i, price in enumerate(prices): #첫번쨰 가격부터 마지막 가격까지..
        second = 0 # 0초부터 계산.
        for after_price in prices[i+1:]:
            second = 1 + second
            #i + 1번빼 부터 비교를 했을떄, 즉 다음거부터 비교를 했을때 
            answer[i] = second
            if after_price < price:
                break #값이 작은게 나오면, 중간에 리턴
    return answer


from typing import List


def is_valid_skill_tree(valid_skill: str, user_skill_tree: str) -> bool:
     return valid_skill.startswith(''.join(filter(lambda x: x in valid_skill, user_skill_tree)))

def solution(skill:str , skill_trees: List[str]) -> int:
    return sum([is_valid_skill_tree(skill, skill_tree) for skill_tree in skill_trees])


def is_valid_skill_tree(valid_skill: str, user_skill_tree: str):
     extract_user_skill = ''.join(list(dict.fromkeys(filter(lambda x: x in valid_skill, user_skill_tree))))
     return valid_skill.startswith(extract_user_skill)

def solution(skill:str , skill_trees: List[str]):
    return len([True for skill_tree in skill_trees
        if is_valid_skill_tree(skill, skill_tree)])