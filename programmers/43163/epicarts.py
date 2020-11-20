def is_dfs_success(word, current_word):  # 하나만 다른지 검사,
    s_count = 0
    for i, s in enumerate(word):
        if s != current_word[i]:  # 같지 않다면,
            s_count += 1
        if s_count > 1:  # 두개이상 나오면 더 볼 필요도 없
            return False
    return True


def dfs(depth, target, current_word, words):
    global count

    # 끝까지 들어가기전에 count 보다 커지면 return
    # 효율성 향상을 위함
    if count < depth:
        return

    if target == current_word:  # 같은 단어가 나오
        count = depth
        return

    for word in words:  # 같은게 1개인 단어만 들어가는 for 문

        if is_dfs_success(word, current_word):  # 단어가 한개이어야만 가능
            next_words = words[:]
            next_words.remove(word)
            dfs(depth + 1, target, current_word=word, words=next_words)

count = 999999

def solution(begin, target, words):
    if target in words:
        dfs(0, target, current_word=begin, words=words[:])
    else:
        return 0
    return count
