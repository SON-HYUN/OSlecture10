from typing import *

count = 0


def kmp_pattern_search(txt: str, pat: str) -> int:
    skip_table: list = []
    pat_idx = 0
    txt_idx = 0
    global count

    for i in range(1, len(pat)):
        count += 1
        if pat[i] == pat[pat_idx]:
            pat_idx += 1
            skip_table.append(pat_idx)
        else:
            pat_idx = 0
            skip_table.append(0)

    pat_idx = 0
    while txt_idx < len(txt):
        count += 1
        if (txt[txt_idx] == pat[pat_idx]):
            pat_idx += 1
            if pat_idx == len(pat):
                return txt_idx - pat_idx + 1
            txt_idx += 1
            continue
        else:
            if pat_idx == 0:
                txt_idx += 1
                continue
            pat_idx = skip_table[pat_idx - 1]
            continue
    return txt_idx


if __name__ == '__main__':
    string = input('문자열을 입력하세요 ')
    pattern = input('패턴을 입력하세요 ')
    occur_idx = kmp_pattern_search(string, pattern)

    if occur_idx == len(string):
        print('해당 패턴을 찾을 수 없습니다')
    else:
        print(f'{occur_idx + 1}번째 문자부터 시작하는 패턴을 찾았습니다')
        print(f'문자 비교 연산 횟수 : {count}')
