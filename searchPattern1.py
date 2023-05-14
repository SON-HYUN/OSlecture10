from typing import *


count = 0


def bf_pattern_search(txt: str, pat: str) -> int:
    pat_idx = 0
    str_idx = 0
    global count

    while str_idx < len(txt):
        count += 1
        if txt[str_idx] == pat[pat_idx]:
            pat_idx += 1
            if pat_idx == len(pat):
                return str_idx
            str_idx += 1
            continue
        else:
            str_idx -= pat_idx - 1
            pat_idx = 0
            continue

    return str_idx


if __name__ == '__main__':
    string = input('텍스트 입력 ')
    pattern = input('패턴 입력 ')
    occur_point = bf_pattern_search(string, pattern)
    if occur_point == len(string):
        print('패턴이 존재하지 않습니다')
    else:
        print(f'{occur_point-len(pattern) + 2}번째 문자부터 시작하여 일치하는 패턴이 존재합니다')
        print(f'문자 비교 연산 횟수 : {count}')
