def amount_of_pages(summary: int) -> int:
    counted = 0
    _ = [0]
    result = 0

    for i in range(1, 1000000000):
        if counted == summary:
            return i - 1
        else:
            _[0] = str(i)
            counted += len(_[0])


if __name__ == '__main__':
    assert amount_of_pages(5) == 5
    assert amount_of_pages(25) == 17
    assert amount_of_pages(1095) == 401
    assert amount_of_pages(185) == 97
    assert amount_of_pages(660) == 256
