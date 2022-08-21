def reverse_list(lst: list) -> list:
    lst.reverse()
    return lst

# or 
# def reverse_list(lst: list) -> list:
#     return lst[::-1]


if __name__ == '__main__':
    assert reverse_list([]) == []
    assert reverse_list([1,2,3,4]) == [4,3,2,1]
    assert reverse_list([2,4,5,6]) == [6,5,4,2]