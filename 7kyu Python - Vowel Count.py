def get_count(sentence):
    lst_of_vow = ['a', 'e', 'i', 'o', 'u']
    vows = 0

    for i in sentence:
        if i in lst_of_vow:
            vows += 1

    return vows

# def get_count(sentence):
#     return len([x for x in sentence if x in 'aeiou'])


if __name__ == '__main__':
    assert get_count("aeiou") == 5
    assert get_count("y") == 0
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0
    assert get_count("") == 0
    assert get_count("abracadabra") == 5
