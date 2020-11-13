# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve) -> int:
    count = 0
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for i in lost_set:
        if (left :=  i-1) in reserve_set:
            reserve_set.remove(left)
            continue
        elif (right := i+1)  in reserve_set:
            reserve_set.remove(right)
            continue

        count += 1

    return n - count


import unittest

class TestStringMethods(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(solution(5, [2,4], [1,3,5]), 5)
        self.assertEqual(solution(5, [2,4], [3]), 4)

    def test_complex_case(self):
        self.assertEqual(solution(3, [3], [1]), 2)
        self.assertEqual(solution(5, [2,4], [1,3,5]), 5)
        self.assertEqual(solution(5, [2,4], [3]), 4)
        self.assertEqual(solution(5, [2,3,4], [1,2,4,5]), 4)
        self.assertEqual(solution(5, [2,3], [3,4]), 4)
        self.assertEqual(solution(5, [1,2,3,4,5], [1,2,3,4,5]), 5)


if __name__ == '__main__':
    unittest.main()

