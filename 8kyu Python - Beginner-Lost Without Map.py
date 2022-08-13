def maps(a: list) -> list:
    return [i * 2 for i in a]

if __name__ == '__main__':
    assert maps([1, 2, 3]) == [2, 4, 6]
    assert maps([122, 312, 343, 231]) == [244, 624, 686, 462]
    assert maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    assert maps([]) == []