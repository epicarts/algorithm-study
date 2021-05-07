from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = [] # 최종 결과를 담을 변수

        def dfs(index: int, path: str):
            # 탈출 조건, digits의 길이만큼 정답을 찾았다면,
            if len(digits) == len(path):
                result.append(path) # 정답을 추가
                return

            # 모든 자판(그래프)를 탐색해야함.
            # 입력값들을 탐색해야함.
            for i in range(index, len(digits)): # 0 ~ digits_len-1 / 1 ~ digists_len-1 ... digits_len-1 ~ digits_len-1
                # digits[i] 입력받은 digits의 어떤것을 탐색할지
                find_dic = dic[digits[i]]
                # print("단어: ", find_dic)
                for alphabet in find_dic: # '23' 중에 해당되는 dic의 알파벳들
                    # print(path + alphabet, "인덱스: ", index)
                    dfs(i + 1, path + alphabet)

        if digits == "":
            return result

        dfs(0, "")
        return result


digits = "234"
print(Solution().letterCombinations(digits))