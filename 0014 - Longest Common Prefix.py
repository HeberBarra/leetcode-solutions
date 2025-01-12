from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    common_prefix: str = ''
    base_word = strs[0]

    for i in range(len(base_word)):
        try:
            for j in range(1, len(strs)):
                if strs[j][i] != base_word[i]:
                    return common_prefix

            common_prefix += base_word[i]
        except IndexError:
            return common_prefix

    return common_prefix


if __name__ == '__main__':
    print(longest_common_prefix(['flower', 'flow', 'flight']))
    print(longest_common_prefix(['dog', 'racecar', 'car']))
