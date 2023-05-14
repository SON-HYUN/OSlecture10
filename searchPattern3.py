from typing import *


count: int = 0


def bm_search_pattern(txt: str, pat: str) -> int:
    skip_table: dict = {}
    global count
    for i in range(len(pat) - 1):
        count += 1
        skip_table[str(pat[i])] = len(pat) - i - 1
    skip_table[str(pat[len(pat) - 1])] = len(pat)
    count += 1

    txt_idx: int = len(pat) - 1
    pat_idx: int = len(pat) - 1

    while txt_idx < len(txt):
        count += 1
        if txt[txt_idx] == pat[pat_idx]:
            pat_idx -= 1
            if pat_idx == -1:
                return txt_idx
            txt_idx -= 1
            continue
        else:
            if str(txt[txt_idx]) in skip_table:
                txt_idx += skip_table.get(str(txt[txt_idx]))
                pat_idx = len(pat) - 1
                continue
            else:
                txt_idx += len(pat)
                pat_idx = len(pat) - 1
                continue
    return txt_idx


if __name__ == '__main__':
    string: str = input('문자열을 입력하세요 ')
    pattern: str = input('패턴을 입력하세요 ')
    occur_idx: int = bm_search_pattern(string, pattern)

    if occur_idx >= len(string):
        print('해당 패턴을 찾을 수 없습니다')
    else:
        print(f'{occur_idx + 1}번째 문자부터 시작하는 패턴을 찾았습니다')
        print(f'문자 비교 연산 횟수 : {count}')
