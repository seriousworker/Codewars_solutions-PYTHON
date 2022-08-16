def fibonacci(n: int) -> int:
    start_siq = [0, 1]

    if n < 2:
        return start_siq[n]
    else:
        for i in range(n + 1):
            start_siq.append(start_siq[i] + start_siq[i + 1])
        return start_siq[n]


""" or 

def fibonacci(n: int) -> int:
    start_seq = [0, 1]
    sum_number = 0

    if n < 2:
        return start_seq[n]
    else:
        m = n - 1
        while m > 0:
            sum_number = start_seq[0] + start_seq[1]
            start_seq[0] = start_seq[1]
            start_seq[1] = sum_number
            m -= 1

    return start_seq[1]
    
    """


if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(34) == 5702887
    assert fibonacci(299) == 137347080577163115432025771710279131845700275212767467264610201
