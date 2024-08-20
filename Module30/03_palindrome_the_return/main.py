from collections import Counter


def can_be_poly(line: str) -> bool:
    cnt = Counter(line)
    extra = list(filter(lambda x: x % 2, cnt.values()))

    return len(extra) <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
print(can_be_poly('арозаупаланалапуазора'))