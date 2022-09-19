def tidyNumber(numb: int) -> bool:
    previous = '0'

    for digit in str(numb):
        if digit < previous:
            return False
        previous = digit
    return True

"""
def tidyNumber(numb: int) -> bool:
    s = list(str(numb))
    return s == sorted(s)
    
"""


if __name__ == '__main__':
    assert tidyNumber(12) == True
    assert tidyNumber(102) == False
    assert tidyNumber(9672) == False
    assert tidyNumber(2789) == True
