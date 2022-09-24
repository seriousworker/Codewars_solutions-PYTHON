def duplicate_encode(word: str) -> str:
    lower_word = word.lower()
    temp_lst = []

    for c in lower_word:
        if lower_word.count(c) > 1:
            temp_lst.append(')')
        else:
            temp_lst.append('(')

    return ''.join(temp_lst)


if __name__ == '__main__':
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("

