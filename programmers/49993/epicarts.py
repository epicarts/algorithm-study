def solution(skill, skill_trees):
    count = 0 #사용가능한 스킬 트리 횟수 카운트

    for skill_tree in skill_trees: #스킬트리 하나씩 검증
        non_learn_skill_list = list(skill) #배우지 않은 스킬 리스트 생성
        skill_check = True # 스킬 체크면 통과

        for skill_to_learn in skill_tree: #찍은 스킬 하나씩 돌면서 검증
            #이미 배운 스킬인가?? 그러면 패스

            # if skill_to_learn in non_learn_skill_list: #현재 스킬이 배우지 않은 스킬에 있는가?
                
            print(skill_to_learn)
            for i, essential_skill in enumerate(non_learn_skill_list): #선행스킬에 해당 스킬 있는가?
                print(i, non_learn_skill_list)
                if essential_skill == skill_to_learn: # 만약 선행스킬에 있으면 들어가는데,
                    if i == 0: #첫번째로 나왓을경우 배우면됨.
                        non_learn_skill_list.pop(0)
                    else: #두번째 이후로 나오면.
                        skill_check = False
                        print('배울 수 없는 스킬')
                    break
                # 선행스킬이 있다면 배웠는가? 
            if skill_check == False: #스킬체크 실패시 리턴
                break
        if skill_check == True:
            count += 1 # 성공적
            print("성공적", count)

    return count

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
skill_trees = ["BACDE"]
skill_trees = ["CBADF"]

c = solution(skill, skill_trees)
