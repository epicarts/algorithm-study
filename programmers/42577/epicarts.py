def solution(phone_book):
    for i, phone_i in enumerate(phone_book):
        for j, phone_j in enumerate(phone_book):
            if i != j and phone_i.startswith(phone_j, 0): # 자기자신이 아니고, 
                return False
    return True
